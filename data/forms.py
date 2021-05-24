from django import forms

class CountryForm(forms.Form):
    country_name = forms.CharField(label='Country')