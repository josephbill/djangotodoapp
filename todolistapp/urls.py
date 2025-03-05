from django.urls import path
from . import views


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:index>', views.delete_task,name="delete_task"),
    path('complete/<int:index>', views.mark_complete,name='mark_complete'),
]









