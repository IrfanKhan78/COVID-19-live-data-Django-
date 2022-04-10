from django.shortcuts import render,redirect

from .forms import CountryForm

import requests
from datetime import date
    

def data_view(request):    


    url = "https://covid-193.p.rapidapi.com/statistics"

    headers = {
        "X-RapidAPI-Host": "covid-193.p.rapidapi.com",
        "X-RapidAPI-Key": "0849de3565msh151e07564470597p153d6fjsn7c5497a652a2"
    }

    form = CountryForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            country_name = form.cleaned_data.get("country")
    else:
        country_name = "USA"


    response = requests.request("GET", url, headers=headers).json()
    data = response["response"]

    for i in range(len(data)-1):
        if data[i]["country"] == country_name:
            country = country_name
            population = data[i]["population"]
            total_cases = data[i]["cases"]["total"]
            new_cases = data[i]["cases"]["new"]
            critical_cases = data[i]["cases"]["critical"]
            recovered = data[i]["cases"]["recovered"]
            deaths = data[i]["deaths"]["total"]


    todays_date = date.today()
    day = todays_date.day
    month = todays_date.month
    year = todays_date.year

    context = {
        "country": country,
        'population' : population,
        'total' : total_cases,
        'new' : new_cases,
        'critical' : critical_cases,
        'recovered' : recovered,
        'deaths' : deaths,
        'day' : day,
        'month' : month,
        'year' : year,
        'form' : form
    }
    

    return render(request, 'data/view.html', context)
