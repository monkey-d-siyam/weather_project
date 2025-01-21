from celery import shared_task
from .models import Weather
from .utils import get_weather_data

@shared_task
def update_weather():
    cities = Weather.objects.values_list('city', flat=True).distinct()
    for city in cities:
        data = get_weather_data(city)
        if data:
            weather = Weather.objects.filter(city=city).latest('date')
            weather.temperature = data['temperature']
            weather.description = data['description']
            weather.humidity = data['humidity']
            weather.wind_speed = data['wind_speed']
            weather.icon = data['icon']
            weather.save()
