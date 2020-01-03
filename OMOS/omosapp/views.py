from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.
from django.utils import timezone

from omosapp.forms import LoginUser
from omosapp.models import SystemUser, NavigationContent


def home(request):
    navigationcontents = NavigationContent.objects.all()
    return render(request, 'omosapp/index.html', {'navigationcontents': navigationcontents})


def register(request):
    return render(request, 'omosapp/register.html', {})


def account(request):
    return render(request, 'omosapp/account.html', {})


def addresses(request):
    return render(request, 'omosapp/addresses.html', {})


def changepassword(request):
    return render(request, 'omosapp/changePassword.html', {})


def chart(request):
    return render(request, 'omosapp/chart.html', {})


def clientinfo(request):
    return render(request, 'omosapp/clientinfo.html', {})


def clientorders(request):
    return render(request, 'omosapp/clientorders.html', {})


def forgetpassword(request):
    return render(request, 'omosapp/forgetPassword.html', {})


def search(request):
    return render(request, 'omosapp/restaurant.html', {})


def myclients(request):
    return render(request, 'omosapp/myclients.html', {})


def myorders(request):
    return render(request, 'omosapp/myorders.html', {})


def myprofile(request):
    return render(request, 'omosapp/myprofile.html', {})


def order(request):
    return render(request, 'omosapp/order.html', {})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('home')
        else:
            error_message = "*Wrong Password or Username."
            form.clean()
    else:
        error_message = ""
        form = AuthenticationForm()

    return render(request, 'omosapp/login.html', {'form': form, 'error_message': error_message})











