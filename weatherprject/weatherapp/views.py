from django.shortcuts import render, redirect
from .form import CityTab, City
import requests
from django.contrib import messages

def home(request):
    form = CityTab()
    url = "http://api.openweathermap.org/data/2.5/weather?q={},&appid=ffe2229e61e85853664785ece624d010&units=metric"
    if request.method == 'POST':
        form = CityTab(request.POST)
        if form.is_valid():
            CityNme = form.cleaned_data['name']
            CityCont =  City.objects.filter(name=CityNme).count()
            if CityCont == 0:
                res = requests.get(url.format(CityNme)).json()
                if res['cod'] == 200:
                    form.save()
                    messages.success(request," "+CityNme+" Added City successfully....!")
                else:
                    messages.error(request, "This City name not Available in API!....")
            else:
                return messages.error(request, "City name already Exist....")
    
    cities = City.objects.all()
    data=[]
    for city in cities:        
        res = requests.get(url.format(city)).json()
        city_weather = {
            'city':city,
            'temprature':res['main']['temp'],
            'description':res['weather'][0]['description'],
            'country':res['sys']['country'],
            'icon':res['weather'][0]['icon'] 
            
        }
        data.append(city_weather)
    
    context = {'form':form,'data':data}
    
    return render(request, 'weatherapp.html', context)

def delete_city(request, CName):
    cityname = City.objects.get(name=CName)
    cityname.delete()
    messages.success(request, "City is Removed Successfully...!")
    return redirect('home')