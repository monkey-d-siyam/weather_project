from django.apps import AppConfig

class ForecastConfig(AppConfig):
    name = 'forecast'

    def ready(self):
        import forecast.signals