from django.shortcuts import render
from .utils import get_weather_data

def index(request):
    weather_data = None
    if 'city' in request.GET:
        city = request.GET['city']
        weather_data = get_weather_data(city)
    return render(request, 'forecast/index.html', {'weather_data': weather_data})
