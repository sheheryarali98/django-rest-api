"""App views"""
from rest_framework.viewsets import ModelViewSet
from auth_api.models import User

from .serializers import ProfileSerializer


class ProfileViewSet(ModelViewSet):  # pylint:disable=too-many-ancestors
    """Handle creating, updating and deleting a user profile"""
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
