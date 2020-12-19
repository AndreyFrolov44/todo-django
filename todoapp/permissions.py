from rest_framework.permissions import BasePermission


class IsAuthorTodo(BasePermission):
    """
    Allows access only to authenticated users.
    """

    # def has_object_permission(self, request, view, obj):
    #     print('-------------------------------')
    #     print(obj.author)
    #     print(request.user)
    #     print('-------------------------------')
    #     return bool(obj.author == request.user and request.user.is_authenticated)

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

