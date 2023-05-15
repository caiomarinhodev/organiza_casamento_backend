from django.apps import AppConfig


class AppOrganizaConfig(AppConfig):
    name = 'app'

    def ready(self):
        import app.signals
