from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'pages/index.html')

def aliments(request):
    return render(request, 'pages/aliments.html')

def mentions(request):
    return render(request, 'pages/mentions.html')

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    form = UserCreationForm()
    context = {'form' : form}
    return render(request, 'pages/registration.html', context)
