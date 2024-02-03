# todo_app/urls.py
from django.urls import path
from todo_app.views import *
urlpatterns = [
    path('tasks/', task_list, name='task_list'),
    path('tasks/show/', show_task, name='show_task'),  # Add this line
    path('tasks/update/<int:task_id>/', update_task, name='update_task'),
    path('tasks/delete/<int:task_id>/', delete_task, name='delete_task'),
]
