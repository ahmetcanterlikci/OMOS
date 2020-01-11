from django.urls import path

from omosapp import views

urlpatterns = [
    path('login', views.login_view, name='login_view'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('personalinfo', views.account, name='personalinfo'),
    path('addresses', views.addresses, name='addresses'),
    path('changepassword', views.changepassword, name='changepassword'),
    path('chart', views.chart, name='chart'),
    path('clientinfo', views.clientinfo, name='clientinfo'),
    path('clientorders', views.clientorders, name='clientorders'),
    path('forgetpassword', views.forgetpassword, name='forgetpassword'),
    path('search', views.search, name='search'),
    path('myclients', views.myclients, name='myclients'),
    path('myorders', views.myorders, name='myorders'),
    path('myprofile', views.myprofile, name='myprofile'),
    path('order', views.order, name='order'),
    path('exit', views.exit_view, name='exit_view'),
    path('base', views.base_view, name='base'),
]