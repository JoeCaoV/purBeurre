from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'pages/index.html')

def aliments(request):
    return render(request, 'pages/aliments.html')

def mentions(request):
    return render(request, 'pages/mentions.html')

def registration(request):
    form = UserCreationForm()
    context = {'form' : form}
    return render(request, 'pages/registration.html', context)
