from django.apps import AppConfig


class AfbcoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "afbcore"

    def ready(self):
        pass
