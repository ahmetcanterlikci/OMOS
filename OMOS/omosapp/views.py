from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.utils import timezone

from omosapp.forms import LoginUser
from omosapp.models import SystemUser, NavigationContent, MyProfileContent


def home(request):
    if request.user.is_authenticated:
        navigationcontents = NavigationContent.objects.filter(usertype='valid')
    else:
        navigationcontents = NavigationContent.objects.filter(usertype='visitor')
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
    if request.user.is_authenticated:
        userprofile = SystemUser.objects.filter(user__username__exact=request.user.username)

        if userprofile.filter(is_customer__exact=True).count() > 0:
            myprofilecontents = MyProfileContent.objects.filter(usertype='customer')
        elif userprofile.filter(is_client__exact=True).count() > 0:
            myprofilecontents = MyProfileContent.objects.filter(usertype='client')
        else:
            myprofilecontents = MyProfileContent.objects.filter(usertype='manager')

        return render(request, 'omosapp/myprofile.html', {'myprofilecontents': myprofilecontents})
    else:
        myprofilecontents = MyProfileContent.objects.filter(usertype='none')
        return render(request, 'omosapp/myprofile.html', {'myprofilecontents': myprofilecontents})


def order(request):
    return render(request, 'omosapp/order.html', {})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            error_message = "*Wrong Password or Username."
            form.clean()
    else:
        error_message = ""
        form = AuthenticationForm()

    return render(request, 'omosapp/login.html', {'form': form, 'error_message': error_message})


def exit_view(request):
    if request.method == "GET":
        return render(request, 'omosapp/exit.html', {})
    else:
        if request.method == "POST" and 'leaveYes' in request.POST:
            logout(request)
            return redirect('home')
        else:
            return redirect('home')












