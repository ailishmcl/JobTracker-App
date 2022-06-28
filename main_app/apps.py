from django.apps import AppConfig


class MainAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_app'

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        print("testing")
        return users.signals