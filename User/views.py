from django.contrib.auth import authenticate, login, forms, logout
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View
from User.forms import *
from User.models import User


# Create your views here.


class Register(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'Auth/register.html', {'form': form})


    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            messages.success(request, f'Account created for {username}!')
            return redirect('Core:home')  # Redirect to the home page after successful registration
        else:
            errors = form.errors
            print(errors)
        return render(request, 'Auth/register.html', {'form': form})


class Login(View):
    def get(self, request):
        # Your view logic for the HTTP GET method goes here
        return render(request, 'Auth/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page or dashboard
            return redirect('Core:home')
        else:
            # Authentication failed
            messages.error(request, 'Invalid username or password.')
        return HttpResponse("This is a POST request response")


class Logout(View):
    def get(self, request):
        logout(request)
        # Your view logic for the HTTP GET method goes here
        return redirect('Core:home')

    def post(self, request):
        # Your view logic for the HTTP POST method goes here
        return HttpResponse("This is a POST request response")