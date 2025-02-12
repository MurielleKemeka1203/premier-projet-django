from django import forms
from listings.models import Band, Listings

class ContactUsForm(forms.Form):
   name = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)

class BandForm(forms.Form):
   name = forms.CharField(max_length=100)
   biography = forms.CharField(max_length=1000)
   year_formed = forms.IntegerField(min_value=1900, max_value=2021)
   official_homepage = forms.URLField(required=False)

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        exclude = ('active', 'official_homepage')  # ajoutez cette ligne