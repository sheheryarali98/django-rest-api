"""App views"""
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from .permissions import IsUpdatingOwnPostOrAdmin
from .serializers import PostSerializer
from .models import Post


class PostViewSet(ModelViewSet):  # pylint:disable=too-many-ancestors
    """Handle creating, updating and deleting posts"""
    permission_classes = [IsUpdatingOwnPostOrAdmin, IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete']
