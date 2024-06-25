from rest_framework import permissions


class UserPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return bool(request.user.is_authenticated and obj==request.user)
        
    def has_permission(self, request, view):
        
        if view.basename == 'Users':
            if request.user.is_anonymous:
                return request.method in permissions.SAFE_METHODS
            return request.user.is_authenticated
        

        
    