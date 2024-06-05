from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls.base import reverse_lazy
from django.http import HttpResponseRedirect
from django.conf import settings
from .models import User
from .forms import RegisterForm
from .backends import EmailBackend

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'user_management/register.html', {'form': form})

def login_view(request):
    AUTH_BACKEND = settings.AUTHENTICATION_BACKENDS[0]
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email,password)
        all_users = User.objects.all()
        print(all_users)

        obj_auth = EmailBackend()
        
        user = obj_auth.authenticate(request, email=email, password=password)
        if user is not None:
            print("verified user")
            login(request, user, backend=AUTH_BACKEND)
            return HttpResponseRedirect(reverse_lazy('view_tasks'))
        else:
            return render(request, 'user_management/login.html', {'error': 'Invalid credentials'})
    return render(request, 'user_management/login.html')
