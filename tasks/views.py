from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                #Register User
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                print('User saved')
                login(request,user)
                return redirect('tasks')
            except Exception as e:
                print('Exception: %s' % e)
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'User already exists'.format(e.args)
                })
        # return Message
        print('Password')
        return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Password dont match'
                })

def task_view(request):
    return render(request, 'tasks.html', {
        'tasks': ['Task 1', 'Task 2', 'Task 3']
    })

def logout_session(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')