from rest_framework import permissions

# Разрешения текущего пользователя
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated or request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # return obj.user == request.user or request.user.is_staff
        return  obj.user == request.user





