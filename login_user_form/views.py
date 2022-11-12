from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from .models import *

# Create your views here.
def index(request): 
    return render(request, "index.html")

def signin(request):
    if request.method == "POST":
        fname = request.POST['fname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        #Profile.objects.create(
         #   user = user_obj,
        #)
        myuser = User.objects.create_user(username, email, password)
        myuser.fullname = fname

        myuser.save()
        messages.success(request, "Your account has been created successfuly.")

        return redirect("login")
    return render(request, "signin.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return render(request, "index.html")
        else:
            messages.error(request, "Bad Credentials")
            return redirect("login")

    return render(request, "login.html")

def logout(request):
    auth_logout(request)
    return render(request, "index.html")