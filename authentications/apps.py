from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'authentications'

    def ready(self):
        import authentications.signals
