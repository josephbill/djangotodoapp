from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser
from todolistapp.models import Task, Taskers
from .serializers import TaskersSerializer, TaskSerializer
from rest_framework.response import Response

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
# class TaskListCreate(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     # THIS WILL ALLOW LOGS OF THE REQUEST FROM THE ANDROID APP>
#     def create(self, request, *args, **kwargs):
#         print("🔥 ANDROID PAYLOAD RECEIVED:", request.data)
#         return super().create(request, *args, **kwargs)

class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    parser_classes = [MultiPartParser, FormParser]
    # THIS WILL ALLOW LOGS OF THE REQUEST FROM THE ANDROID APP>
    def create(self, request, *args, **kwargs):
        print("🔥 ANDROID PAYLOAD RECEIVED:", request.data)

        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print("❌ Serializer Errors:", serializer.errors)
            return Response(serializer.errors, status=400)

        self.perform_create(serializer)
        return Response(serializer.data, status=201)


class TaskRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer













