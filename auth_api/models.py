"""App models"""
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models


class UserManager(BaseUserManager):
    """Custom manager for creating users"""

    def create_user(self, email, name, password=None):
        """Create a user"""

        if not password:
            raise ValueError('Password is required')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        """Create a super user"""
        if not password:
            raise ValueError('Password is required')

        user = self.create_user(email, name, password)
        user.is_staff = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """Custom user model"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return str(self.email)

    def has_perm(self, perm, obj=None):  # pylint:disable=unused-argument,no-self-use
        """Check if the user has a specific permission"""
        return True

    def has_module_perms(self, app_label):  # pylint:disable=unused-argument,no-self-use
        """Check if the user has access to a specific app"""
        return True

    def get_full_name(self):
        """Return the full name of the user"""
        return str(self.email)

    def get_short_name(self):
        """Return the short name of the user"""
        return str(self.email)
