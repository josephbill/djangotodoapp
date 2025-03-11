from django.urls import path
from . import views


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('addTasker/', views.add_tasker, name='add_tasker'),
    path('delete/<int:task_id>', views.delete_task,name="delete_task"),
    path('complete/<int:task_id>', views.mark_complete,name='mark_complete'),
]









