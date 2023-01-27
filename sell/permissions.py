from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.methods in SAFE_METHODS or
            request.user and
            request.user == obj.owner
        )
