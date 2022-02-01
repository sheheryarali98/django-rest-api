"""App permissions"""
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsUpdatingOwnPostOrAdmin(BasePermission):
    """Check if user is updating own profile"""

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or request.user.id == obj.id or request.user.is_staff:
            return True

        return False
