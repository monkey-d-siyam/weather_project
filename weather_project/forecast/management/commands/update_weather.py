from django.core.management.base import BaseCommand
from forecast.models import Weather
from forecast.utils import get_weather_data

class Command(BaseCommand):
    help = 'Update weather data every hour'

    def handle(self, *args, **kwargs):
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
        self.stdout.write(self.style.SUCCESS('Successfully updated weather data'))