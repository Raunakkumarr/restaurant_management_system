#Importing Libraries
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

def login_anywhere(request):
    user_name = request.POST['username']
    password = request.POST['password']
    user = authenticate(request=request, username=user_name, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, "You're successfully logged in...")
    else:
        messages.success(request, "There was an error logging in, please try again...")
