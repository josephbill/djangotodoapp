from rest_framework import generics
from todolistapp.models import Task, Taskers
from .serializers import TaskersSerializer, TaskSerializer
# Create your views here.

# CRUD operations for the Tasker
# Listing and creating
class TaskerListCreate(generics.ListCreateAPIView):
    queryset = Taskers.objects.all()
    serializer_class = TaskersSerializer

#  updating and deleting
class TaskerRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Taskers.objects.all()
    serializer_class = TaskSerializer

# CRUD OPERATIONS FOR TASKS
class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer













