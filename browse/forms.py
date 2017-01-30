from django import forms
from data.models import UserProfile,message
class teamNumForm(forms.ModelForm):
    #team_number = forms.IntegerField(label='team number:')
    #shirt_url = forms.CharField(max_length=400)
    class Meta:
       model = UserProfile
       fields = ["team","wanted","shirtImg","post"] # list of fields you want from model
       #exclude=["user"]
class messageForm(forms.ModelForm):
    class Meta:
        model=message
        fields=["content"]


class browseForm(forms.Form):
    # search = forms.CharField(label="search", max_length=100)
    search = forms.IntegerField()

    SortOptions = (
        (1, ("number")),
        (2, ("date")),
    )
    sortBy = forms.ChoiceField(choices=SortOptions)
