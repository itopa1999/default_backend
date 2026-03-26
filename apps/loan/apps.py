from django.apps import AppConfig


class LoanConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.loan'
    label = 'loans'  # This sets the app label to 'loans' instead of the default 'loan'

    
    def ready(self):
        import apps.loan.signals

