from rest_framework import permissions


class DenyAll(permissions.BasePermission):
    """
    Custom permission to deny all requests
    """

    def has_permission(self, request, view):
        return False
