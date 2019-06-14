from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from website.models import Product

def home(request):
    """Home Page"""
    return render(request, 'pages/index.html')

def product(request, product_name):
    name = product_name
    try:
        product = Product.objects.get(name=name)
        context = {'product' : product}
    except:
        context = {'error' : 'Ce produit n\'existe pas dans notre base de données.'}
    else:
        try:
            alternatives = Product.objects.filter(nutriscore__lt=product.nutriscore,
                                                  category=product.category)
            if alternatives:
              context['alternatives'] = alternatives
            else:
                raise Exception()
        except:
            context['no_alternatives'] = 'Aucun meilleur produit trouvé'

    return render(request, 'pages/product.html', context)

def search(request):
    search = request.get['name']
    products = Product.objects.filter(name__contains=search)
    if len(products):
        pass


def aliments(request):
    return render(request, 'pages/aliments.html')

def mentions(request):
    """Legales mentions page"""
    return render(request, 'pages/mentions.html')

def registration(request):
    """Page to create an account"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserCreationForm()
    context = {'form' : form}
    return render(request, 'pages/registration.html', context)

def connection(request):
    """page to log in"""
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    context = {'form' : form}
    return render(request, 'pages/connexion.html', context)

def disconnection(request):
    """Please, the name is clear enough"""
    logout(request)
    return redirect('home')
