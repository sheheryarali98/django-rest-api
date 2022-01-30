"""App urls"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProfileViewSet

router = DefaultRouter()
router.register('', ProfileViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]
