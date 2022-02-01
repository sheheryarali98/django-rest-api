"""App configuration"""
from django.apps import AppConfig


class PostsApiConfig(AppConfig):
    """Class used to configure fields related to app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts_api'
