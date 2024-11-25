from django.apps import AppConfig


class AuditappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auditapp'


    def ready(self):
        import auditapp.signals  
