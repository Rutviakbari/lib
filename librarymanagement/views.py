from django import views
import django
from django.shortcuts import redirect, render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
    
def index(request):
    return render(request,'index.html')

    
def about(request):
    return render(request,'about.html')

    
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == "POST":
     fname=request.POST.get('firstname')
     lname=request.POST.get('lastname')
     uname=request.POST.get('username')  
     email=request.POST.get('email')
     pass1=request.POST.get('pass1')
     pass2=request.POST.get('pass2')
     if pass1!=pass2:
         messages.warning(request,'password does not match')
         return redirect ('register')
     elif User.objects.filter(username=uname).exists():
         messages.warning(request,'username allready taken')
         return redirect ('register')
     elif User.objects.filter(email=email).exists():
         messages.warning(request,'email allready taken')
         return redirect ('register')
     else:
       user= User.objects.create_user(first_name=fname,last_name=lname, username=uname,email=email,password=pass1)
       user.save()
       messages.success(request,'user has been registered successfully')
       return redirect('login')
    return render(request,'register.html')

def user_login(request):
    if request.method == "POST":
     username=request.POST.get('username')
     password=request.POST.get('password')
     user=authenticate(request,username=username,password=password)
     if user is not None:
        login(request, user)
        return redirect('home')
     else:
         messages.warning(request,'invalid credentials')
         return redirect('login')
     
    return render(request,'login.html')

    
   
def user_logout (request):
    logout(request)
    return redirect('/')