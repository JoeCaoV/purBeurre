from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.registration, name='register'),
    path('aliments', views.aliments, name="aliments"),
    path('mentions', views.mentions, name="mentions"),
    path('connection', views.login, name="login"),
    path('disconnection', views.disconnection, name='logout'),
]