from django.urls import path

from omosapp import views

urlpatterns = [
    path('login', views.login_view, name='login_view'),
    path('home', views.home, name='home'),
]