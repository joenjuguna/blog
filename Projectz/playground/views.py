
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post,Users
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib import messages


# Create your views here.
def say_hello(request):
    return HttpResponse('Hello World')

def index(request):
    posts=Post.objects.all()
    return render(request,'index.html',{'posts':posts})
def post(request,pk):
    posts = Post.objects.get(id=pk)
    return render(request,'post.html', {'posts':posts})

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if Users.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            if Users.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user=users(username=username, email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Passwords DO NOT match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is  None:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')

        else:
            auth.login(request, user)
            return redirect('index')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')