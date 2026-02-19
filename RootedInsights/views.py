from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def login_view(request):
    return render(request,'login.html')

def logout_view(request):
    return render(request,'logout.html')

def register_view(request):
    return render(request,'register.html')