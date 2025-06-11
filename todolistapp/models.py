from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
# create a custom user model
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True, blank=True,
                                    null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/',
                                        blank=True, null=True)

    def __str__(self):
        return self.username


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
    image = models.ImageField(upload_to='task_images/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # here establishing a one to many relationship using a FK
    tasker = models.ForeignKey(Taskers, on_delete=models.SET_NULL, null=True,
                               blank=True)
    # this tags the user who creates the task
    # run migration after change
    # python manage.py makemigrations appname  /   python manage.py migrate
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL,
                             null=True, blank=True)

    ## save the image field url
    def save(self,*args,**kwargs):
        if self.image:
            self.image_url = self.image.url
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title

    """
    1. python manage.py migrate todolistapp zero
    2. python manage.py makemigrations 
    3. python manage.py migrate 
    """



















