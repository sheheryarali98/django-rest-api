"""App serializers"""
from rest_framework.serializers import ModelSerializer

from auth_api.models import User


class ProfileSerializer(ModelSerializer):
    """Serializer for user profiles"""

    class Meta:  # pylint: disable=missing-class-docstring,too-few-public-methods
        model = User
        fields = ['id', 'email', 'name', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        """Create a new user profile"""
        user = User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )

        return user

    def update(self, instance, validated_data):
        """Update an existing user profile"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
