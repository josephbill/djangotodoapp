from rest_framework import serializers
from todolistapp.models import Task,Taskers

class TaskersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taskers
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    #  this variable will handle the get process
    tasker_detail = TaskersSerializer(source='tasker', read_only=True)
    # this variable will handle the post requests
    tasker = serializers.PrimaryKeyRelatedField(queryset=Taskers.objects.all())

    class Meta:
        model = Task
        fields = '__all__'


