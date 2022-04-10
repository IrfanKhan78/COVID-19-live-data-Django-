from django import forms
import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    "X-RapidAPI-Host": "covid-193.p.rapidapi.com",
    "X-RapidAPI-Key": "0849de3565msh151e07564470597p153d6fjsn7c5497a652a2"
}

response = requests.request("GET", url, headers=headers).json()
data = response["response"]

COUNTRIES_CHOICES = []
countries = []
continents = ["Asia", "Africa", "North America", "South America", "Europe"]

# getting the drop down for the country
for i in range(0, len(data) - 1):
    if (data[i]['country'] not in countries and data[i]['country'] != "All" and data[i]['country'] not in continents):
        name = data[i]['country']
        countries.append(name)
    else:
        continue

countries.sort()
for i in range(len(countries)-1):
    name = countries[i]
    tup = (name,name)
    COUNTRIES_CHOICES.append(tup)

####################################################


class CountryForm(forms.Form):
    country = forms.CharField(label='Country', widget = forms.Select(choices = COUNTRIES_CHOICES), max_length=200)
