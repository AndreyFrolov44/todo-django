from rest_framework import serializers

from .models import TodoBlock, TodoItem


class TodoItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoItem
        exclude = ('block',)


class TodoItemDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoItem
        fields = '__all__'


class TodoBlockSerializer(serializers.ModelSerializer):
    items = TodoItemSerializer(many=True)

    class Meta:
        model = TodoBlock
        fields = '__all__'


class TodoBlockDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoBlock
        fields = '__all__'

