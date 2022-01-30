"""App urls"""
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path(r'login/', TokenObtainPairView.as_view()),
    path(r'refresh/', TokenRefreshView.as_view()),
]
