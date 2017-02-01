from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from data.models import UserProfile,message,shirtImage,teamProfile
from .forms import teamNumForm, messageForm, browseForm
# Create your views here.
#@login_required
def index(request):
    a=shirtImage(team=1984,shirtImg="bleh",year=2015)
    template="browse/index.html"
    context={}
    context["user"]=request.user
    if  not request.user.is_anonymous():#display seperate if not logged in
        priorityTrades=[]
        try:
            UserObj=UserProfile.objects.filter(user=request.user)[0]
        except:
            return redirect('/profile')
        try:
            wanted=UserObj.wanted
            for i in wanted.split(","):
                i=int(i)
                teamMems=UserProfile.objects.filter(team=i,post=True).exclude(shirtCount=0)
                if len(teamMems)>0:
                    priorityTrades.append(teamMems[0])
        except:
            priorityTrades=[]
                    
        context["trades"]=priorityTrades
    return render(request,template,context)

@login_required
def profile(request):
    if request.method == 'POST':
            form = teamNumForm(request.POST)
            if form.is_valid():
                team=form.cleaned_data["team"]
                wanted=form.cleaned_data["wanted"]
                shirtImg=form.cleaned_data["shirtImg"]
                post=form.cleaned_data["post"]
                try:#update existing user object
                    a=UserProfile.objects.get(user=request.user)
                    a.team=team
                    a.wanted=wanted
                    a.shirtImg=shirtImg
                    a.post=post
                    a.save()
                except:#create new user object
                    a=UserProfile(user=request.user,team=team,shirtImg=shirtImg,post=post)
                    a.save()
                return redirect('/profile')
    else:
        try:
            a=UserProfile.objects.filter(user=request.user)[0]
            form = teamNumForm(instance=a)
        except:
            form=teamNumForm()
        
    template="browse/profile.html"
    context={}
    context["user"]=request.user
    context["form"]=form
    #context["teamNumber"]=(UserProfile.objects.get(user=request.user)).team
    #context["url"]=(UserProfile.objects.get(user=request.user)).shirtImg
    return render(request,template,context)
@login_required

def browse(request):
    template = "browse/browse.html"
    context={}
    searchTerm = ""
    if request.method == "POST":
        form = browseForm(request.POST)
        if form.is_valid():
            searchTerm = form.cleaned_data["search"]
            #sortBy = form.cleaned_data["sortBy"]
    else:
        form = browseForm()
    context["form"] = form

    items = UserProfile.objects.filter(post=True)
    if searchTerm != "":
        items = items.filter(team=searchTerm)
    context["items"] = items
    return render(request,template,context)

@login_required
def detail(request,userName):
    selected=User.objects.filter(username=userName)[0]
    
    if request.method == 'POST':
            form = messageForm(request.POST)
            if form.is_valid():
                content=form.cleaned_data["content"]
                
                #find next order element
                lastSent=message.objects.filter(sentBy=request.user,sentTo=selected).order_by("-order")
                lastRecieved=message.objects.filter(sentTo=request.user,sentBy=selected).order_by("-order")
                if (len(lastSent)==0 and len(lastRecieved)==0):
                    nextOrder=0
                elif len(lastSent)==0:
                    nextOrder=lastRecieved[0].order+1
                elif len(lastRecieved)==0:
                    nextOrder=lastSent[0].order+1
                else:
                    if lastSent[0].order>lastRecieved[0].order:
                        nextOrder=lastSent[0].order+1
                    else:
                        nextOrder=lastRecieved[0].order+1
                        
                a=message(sentBy=request.user,sentTo=selected,content=content,order=nextOrder)
                a.save()
                return redirect('/detail/%s'% selected.username)
    else:
        a=UserProfile.objects.filter(user=request.user)[0]
        form = messageForm(instance=a)
    template="browse/detail.html"
    context={}
    
    posting=UserProfile.objects.filter(user=selected)[0]
    context["post"]=posting
    
    myMessages=message.objects.filter(sentBy=request.user,sentTo=selected)
    theirMessages=message.objects.filter(sentBy=selected,sentTo=request.user)
    mergedMessages=[]
    order=0
    while(True):
        currentMessage=theirMessages.filter(order=order)
        if len(currentMessage)==0:
            currentMessage=myMessages.filter(order=order)
            if len(currentMessage)==0:
                break
        mergedMessages.append(currentMessage[0])
        order+=1
    
    
    context["form"]=form
    context["mergedMessages"]=mergedMessages
    return render(request,template,context)

@login_required
def messages(request):
    template="browse/messages.html"
    context={}
    
    messagesTo=message.objects.filter(sentBy=request.user)
    messagesFrom=message.objects.filter(sentTo=request.user)
    activeMessages=[]
    for i in messagesTo:
        if i.sentTo not in activeMessages:
            activeMessages.append(i.sentTo)
    for i in messagesFrom:
        if i.sentBy not in activeMessages:
            activeMessages.append(i.sentBy)
    context["activeMessages"]=activeMessages
    return render(request,template,context)