from rest_framework import serializers
from todo.models import Todo


class TODOSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'todo', 'done']
