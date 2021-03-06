from django.urls import path, include
from . import views
from django.conf.urls import handler500, handler404

handler500 = 'website.views.handler500'
handler404 = 'website.views.handler404'

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.registration, name='register'),
    path('aliments', views.aliments, name="aliments"),
    path('mentions', views.mentions, name="mentions"),
    path('connection', views.connection, name="connection"),
    path('disconnection', views.disconnection, name='logout'),
    path('product/<path:product_name>', views.product, name='product'),
    path('search', views.search, name='search'),
    path('save-alt', views.save_alt, name='save_alt'),
    path('account', views.account, name='account'),
    path('contact', views.contact, name='contact'),
]