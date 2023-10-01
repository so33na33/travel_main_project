

from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import render, redirect

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info("Invalid Username And Password")
            return redirect('login')
    return render(request,"login.html")
# Create your views here.
def register(request):
    if request.method=='POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        uname=request.POST['username']
        pwd=request.POST['password']
        cpwd=request.POST['confirm password']
        if pwd==cpwd:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username Already Exists...")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Exists...")
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=pwd)
                user.save();
                return redirect('login')
        else:
            messages.info(request,"Password Not Matching...")
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')