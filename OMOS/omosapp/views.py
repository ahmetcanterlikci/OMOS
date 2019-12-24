from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.
from django.utils import timezone

from omosapp.forms import LoginUser
from omosapp.models import SystemUser


def home(request):
    return render(request, 'omosapp/index.html', {})


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











