from django import forms
from data.models import UserProfile,message,shirtImage


class teamProfileForm(forms.ModelForm):
    delete = forms.BooleanField(initial=False,required=False)
    class Meta:
        model=shirtImage
        fields = ["year","shirtImg"]
    def __init__(self, *args, **kwargs):
        super(teamProfileForm, self).__init__(*args, **kwargs)

        self.fields["year"].required = True 
        self.fields["shirtImg"].required = True 

    


class teamNumForm(forms.ModelForm):
    team = forms.IntegerField(label='team number:')
    #shirt_url = forms.CharField(max_length=400)
    shirtChoice = forms.ModelChoiceField(queryset=shirtImage.objects.none(),required=False)
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user') #Throws an error if user is not present
        super(teamNumForm, self).__init__(*args, **kwargs)
        qs = shirtImage.objects.filter(team=user.team)
        self.fields['shirtChoice'].queryset = qs
        try:#if user has picked shirt, display
            self.fields["shirtChoice"].initial=user.shirtImg
        except:
            self.fields["shirtChoice"].initial=None
        try:
            self.fields["team"].initial=user.team.team
        except:
            self.fields["team"].initial=None

        
    class Meta:
       model = UserProfile
       fields = ["wanted","post"] # list of fields you want from model
       #exclude=["user"]
       labels = {
            'wanted': ('teams you are interested in:')
            #'shirtImg': ('link to shirt image:'),

        }
       help_texts = {
           #"team": "Your team number",
            #'shirtImg': 'put a direct link to an image of your shirt here',
            "wanted": "put a list of team numbers, formatted like so: 100,200,300"
        }
    field_order=['team','shirtChoice',"wanted","post"]
       
class messageForm(forms.ModelForm):
    class Meta:
        model=message
        fields=["content"]
        labels = {
            'content': ('put your message here:'),
        }
        


class browseForm(forms.Form):
    # search = forms.CharField(label="search", max_length=100)
    search = forms.IntegerField()

    SortOptions = (
        (1, ("number")),
        (2, ("date")),
    )
    #sortBy = forms.ChoiceField(choices=SortOptions)
