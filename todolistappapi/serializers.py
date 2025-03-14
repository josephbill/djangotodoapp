from rest_framework import serializers
from todolistapp.models import Task,Taskers

class TaskersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taskers
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    tasker = TaskersSerializer(read_only=True)
    class Meta:
        model = Task
        fields = '__all__'