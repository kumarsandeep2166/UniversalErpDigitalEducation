from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
#from django.http import HttpResponse, HttpResponseRedirect


def user(request):
    c={}
    return render(request,'user/login.html',c)

def userlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password = password)
        if user is not None and user.is_active:
            login(request, user)
            request.session['username']=username
           
            return redirect('/')
        else:
            return redirect('login.html')
    return render(request, 'user/login.html')

def userlogout(request):
    auth.logout(request)
    return render(request,'user/login.html')


def userinvalid(request):
    return redirect('user/404.html')
            

