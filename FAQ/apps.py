from django.apps import AppConfig

class FaqAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FAQ'

    def ready(self):
        import FAQ.signals