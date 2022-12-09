from rest_framework import permissions
from rest_framework.views import Request, View


class IsAdminOrAuthenticated(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        print(request)
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_superuser:
            return True

        return False
