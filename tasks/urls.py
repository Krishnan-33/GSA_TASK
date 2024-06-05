from django.urls import path
from .views import dashboard, create_task, view_tasks

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('create/', create_task, name='create_task'),
    path('tasks/', view_tasks, name='view_tasks'),
]