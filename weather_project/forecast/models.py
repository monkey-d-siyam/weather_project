from django.db import models

class Weather(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    description = models.CharField(max_length=255)
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    icon = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} - {self.temperature}°C"

from django.contrib.auth.models import User
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.country}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    recent_activities = models.TextField(blank=True)
    favorite_cities = models.ManyToManyField(City, blank=True)

    def __str__(self):
        return self.user.username