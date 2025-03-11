from django.db import models

# Create your models here.
class Taskers(models.Model):
    """custom class to list our taskers"""
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Task(models.Model):
    title = models.CharField(max_length=100, unique=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # here establishing a one to many relationship using a FK
    tasker = models.ForeignKey(Taskers, on_delete=models.SET_NULL, null=True,
                               blank=True)
    def __str__(self):
        return self.title

    """
    1. python manage.py migrate todolistapp zero
    2. python manage.py makemigrations todolistapp
    3. python manage.py migrate 
    """



















