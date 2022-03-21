from rest_framework.viewsets import ModelViewSet
from todo.serializers import TODOSerializer, Todo

class TodoViewSet(ModelViewSet):

    serializer_class=TODOSerializer
    queryset=Todo.objects.all()
