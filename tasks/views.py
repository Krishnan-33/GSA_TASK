from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from user_management.models import User

from datetime import date, time


@login_required
def dashboard(request):
    tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, 'tasks/dashboard.html', {'tasks': tasks})

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return redirect('dashboard')
    else:
        form = TaskForm()
    all_users = User.objects.all()
    return render(request, 'tasks/create_tasks.html', {'form': form,'all_users':all_users})

@login_required
def view_tasks(request):
    tasks = Task.objects.filter(assigned_to_id = request.user.id)
    all_tasks = []
    for t in tasks:
        temp = {}
        temp['task_name'] = t.name
        temp['date'] = t.date_time.date()
        temp['time'] = t.date_time.time()
        temp['assigned_by'] = t.created_by.username
        temp['status'] = t.status
        all_tasks.append(temp)

    return render(request, 'tasks/view_tasks.html', {'tasks': tasks,'all_tasks':all_tasks})
