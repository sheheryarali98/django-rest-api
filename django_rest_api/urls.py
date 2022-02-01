"""Main app urls"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'api/auth/', include('auth_api.urls')),
    path(r'api/profiles/', include('profiles_api.urls')),
    path(r'api/posts/', include('posts_api.urls')),
]
