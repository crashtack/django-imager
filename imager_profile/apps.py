from django.apps import AppConfig


class ImagerProfileAppConfig(AppConfig):
    name = "imager_profile"
    verbose_name = "Imager User Profile"

    def ready(self):
        """code to run when the app is ready"""
        from imager_profile import handlers
