from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


# https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions

class IsAuthenticatedAndReadOnlyOrAdmin(permissions.BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True

        return bool(
            request.method in SAFE_METHODS and
            request.user and
            request.user.is_authenticated
        )


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == SAFE_METHODS:
            return True
        print(bool(request.user and request.user.is_staff))
        return bool(request.user and request.user.is_staff)

