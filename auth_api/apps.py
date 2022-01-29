"""App configuration"""
from django.apps import AppConfig


class AuthApiConfig(AppConfig):
    """Class used to configure fields related to app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth_api'
