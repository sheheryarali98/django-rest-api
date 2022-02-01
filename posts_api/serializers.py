"""App serializers"""
from rest_framework.serializers import ModelSerializer

from .models import Post


class PostSerializer(ModelSerializer):
    """Serializer for posts"""

    class Meta:  # pylint:disable=too-few-public-methods
        model = Post
        fields = [
            'id',
            'title',
            'description',
            'created_on',
            'updated_on',
            'user'
        ]
