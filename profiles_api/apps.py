"""App configuration"""
from django.apps import AppConfig


class ProfilesApiConfig(AppConfig):
    """Class used to configure fields related to app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles_api'
