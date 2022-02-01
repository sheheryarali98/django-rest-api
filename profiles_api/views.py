"""App views"""
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from auth_api.models import User

from .permissions import IsUpdatingOwnProfileOrAdmin
from .serializers import ProfileSerializer


class ProfileViewSet(ModelViewSet):  # pylint:disable=too-many-ancestors
    """Handle creating, updating and deleting a user profile"""
    permission_classes = [IsAuthenticated, IsUpdatingOwnProfileOrAdmin, ]
    authentication_classes = [JWTAuthentication]
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
