from django import forms
from data.models import UserProfile,message



class teamNumForm(forms.ModelForm):
    #team_number = forms.IntegerField(label='team number:')
    #shirt_url = forms.CharField(max_length=400)
    class Meta:
       model = UserProfile
       fields = ["team","wanted","post"] # list of fields you want from model
       #exclude=["user"]
       labels = {
            'wanted': ('teams you are interested in:')
            #'shirtImg': ('link to shirt image:'),

        }
       help_texts = {
           "team": "Your team number",
            #'shirtImg': 'put a direct link to an image of your shirt here',
            "wanted": "put a list of team numbers, formatted like so: 100,200,300"
        }
       
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
