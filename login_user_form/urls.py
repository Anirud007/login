from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('login', views.login, name="login"),
    path('signin', views.signin, name="signin"),
    path('logout', views.logout, name="logout")   
]