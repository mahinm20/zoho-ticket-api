from django.shortcuts import render,redirect
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User


def signUp(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'ticketapi/signup.html',{'error':'username already exists'})

            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'],
                email=request.POST['email'])
                auth.login(request,user)
                return HttpResponse('welcome')
        else:
            return HttpResponse('Passwords must match!')        
    else:
        return render(request,'ticketapi/signup.html')


def login(request):
    if request.method == 'POST':
        
        user = auth.authenticate(username=request.POST['email'],password=request.POST['password'])

        if user is not None:
            auth.login(request, user)
            return HttpResponse('logged in')
        else:
            return render(request, 'ticketapi/login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request, 'ticketapi/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return HttpResponse('Logged out')
