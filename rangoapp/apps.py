from django.apps import AppConfig


class RangoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rangoapp'

    def ready(self):
        import rangoapp.signals
