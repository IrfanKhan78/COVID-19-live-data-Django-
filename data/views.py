from django.shortcuts import render,redirect

from .forms import CountryForm

import requests

import pycountry

# Create your views here.

countries = []
for country in pycountry.countries:
    countries.append(country.name)

def data_view(request):    
    url = "https://covid-193.p.rapidapi.com/statistics"


    # Creating a form and getting country
    form = CountryForm()
    if request.method == 'POST':
        country = request.POST['country_name']                       
    else:  
        country = "USA"       
        

    querystring = {"country": country}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "be7f37114bmsh38c0486c35a5050p1bc1e5jsnf574155ad041"
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    result = response['response'][0]

    # Getting the time
    time = result['time'][:10].split('-')
    day = time[2]
    month = time[1]
    year = time[0]

    # Getting all the datas to be displayed
    population = result['population']
    total_cases = result['cases']['total']
    new_cases = result['cases']['new']
    critical_cases = result['cases']['critical']
    recovered = result['cases']['recovered']
    death = result['deaths']['total']


    context = {
        "country": country,
        'population' : population,
        'total' : total_cases,
        'new' : new_cases,
        'critical' : critical_cases,
        'recovered' : recovered,
        'deaths' : death,
        'day' : day,
        'month' : month,
        'year' : year,
        'form' : form
    }

    return render(request, 'data/view.html', context)
