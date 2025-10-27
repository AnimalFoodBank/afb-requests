from rest_framework import permissions


class DenyAll(permissions.BasePermission):
    """
    Custom permission to deny all requests
    """

    def has_permission(self, request, view):
        return False


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to view and edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Instance must have an attribute named `user`.
        return obj.user == request.user
