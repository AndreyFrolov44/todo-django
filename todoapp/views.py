from rest_framework import generics, permissions
from .serializres import TodoBlockSerializer, TodoBlockDetailSerializer, TodoItemDetailSerializer
from .models import TodoBlock, TodoItem
from .permissions import IsAuthorTodo


class TodoBlockListView(generics.ListAPIView):
    serializer_class = TodoBlockSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return TodoBlock.objects.filter(author=user)


class TodoBlockDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoBlock.objects.all()
    serializer_class = TodoBlockDetailSerializer
    permission_classes = [IsAuthorTodo]


class TodoBlockCreateView(generics.CreateAPIView):
    queryset = TodoBlock.objects.all()
    serializer_class = TodoBlockDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class TodoItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemDetailSerializer
    permission_classes = [IsAuthorTodo]


class TodoItemCreateView(generics.CreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemDetailSerializer
    permission_classes = [permissions.IsAuthenticated]







