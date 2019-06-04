from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.registration, name='registration'),
    path('aliments', views.aliments, name="aliments"),
    path('mentions', views.mentions, name="mentions"),    
]