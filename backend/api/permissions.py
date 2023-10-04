from rest_framework import permissions

# from recipes.models import User

class IsAdminOrReadOnly(permissions.BasePermission):
    """Права для работы с User."""
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_admin
        )


class IsAdminAuthorOrReadOnly(permissions.BasePermission):
    """Редактирование объекта, только владельцам объекта."""
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)



# class IsAdmitOrGetOut(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return (
#             request.user.is_authenticated
#             and request.user.is_admin
#         )