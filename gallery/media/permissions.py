from rest_framework import permissions

class IsOwnerOrShared(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not hasattr(obj, 'owner') or not hasattr(obj, 'shares'):
            return False

        if obj.owner == request.user:
            return True

        shares = obj.shares.filter(users__in=[request.user])
        if request.method in permissions.SAFE_METHODS and shares.count() >= 1:
            return True

        return False
