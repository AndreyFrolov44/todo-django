from rest_framework import generics, permissions
from .serializres import TodoBlockSerializer
from .models import TodoBlock
from.permissions import IsAuthor


class TodoBlockView(generics.ListAPIView):
    queryset = TodoBlock.objects.all()
    serializer_class = TodoBlockSerializer
    # permission_classes = [IsAuthor]

