from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'
    label = 'users'  # This sets the app label to 'users' instead of the default 'user'

    
    def ready(self):
        import apps.users.signals
