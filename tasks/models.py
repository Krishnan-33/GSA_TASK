from django.db import models
from user_management.models import User

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    assigned_to = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='task_created_by', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='Pending')