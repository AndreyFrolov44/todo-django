from rest_framework.permissions import BasePermission


class IsAuthorTodo(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

