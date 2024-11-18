from django.apps import AppConfig


class ManagedServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Managed_services'

    def ready(self):
        import Managed_services.signals
