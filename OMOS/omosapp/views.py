from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
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


def base_view(request):
    return render(request, 'omosapp/base.html', {})


def register(request):
    return render(request, 'omosapp/register.html', {})


def account(request):
    return render(request, 'omosapp/account.html', {})


def addresses(request):
    return render(request, 'omosapp/addresses.html', {})


def changepassword(request):
    if request.method == "POST":
        changepasswordform = PasswordChangeForm(request.user, data=request.POST)
        if changepasswordform.is_valid():
            changepasswordform.save()
            return redirect('changepassword')
    else:
        changepasswordform = PasswordChangeForm(request.user)
        return render(request, 'omosapp/changePassword.html', {'changepasswordform': changepasswordform, })


def chart(request):
    return render(request, 'omosapp/chart.html', {})


def clientinfo(request):
    return render(request, 'omosapp/clientinfo.html', {})


def clientorders(request):
    return render(request, 'omosapp/clientorders.html', {})


def forgetpassword(request):
    return render(request, 'omosapp/forgetPassword.html', {})


def search(request):
    if request.method == "GET":
        clients = SystemUser.objects.filter(is_client=True)
        restaurantcount = clients.filter(clientType='Restaurant').count()
        marketcount = clients.filter(clientType='Market').count()
        distinctrates = clients.values('clientrate').distinct().order_by('clientrate')
        distinctprices = clients.values('clientMinPrice').distinct().order_by('clientMinPrice')

        if request.user.is_authenticated:
            navigationcontents = NavigationContent.objects.filter(usertype='valid')
        else:
            navigationcontents = NavigationContent.objects.filter(usertype='visitor')
        return render(request, 'omosapp/restaurant.html',
                      {'clients': clients, 'distinctrates': distinctrates, 'distinctprices': distinctprices,
                       'navigationcontents': navigationcontents, 'restaurantcount': restaurantcount, 'marketcount': marketcount, })
    else:
        if request.POST.get('searchvalue'):
            searchvalue = request.POST.get('searchvalue')
            clients = SystemUser.objects.filter(is_client=True).filter(clientName__contains=searchvalue)
            restaurantcount = clients.filter(clientType='Restaurant').count()
            marketcount = clients.filter(clientType='Market').count()
            distinctrates = clients.values('clientrate').distinct().order_by('clientrate')
            distinctprices = clients.values('clientMinPrice').distinct().order_by('clientMinPrice')

            if request.user.is_authenticated:
                navigationcontents = NavigationContent.objects.filter(usertype='valid')
            else:
                navigationcontents = NavigationContent.objects.filter(usertype='visitor')
            return render(request, 'omosapp/restaurant.html',
                          {'clients': clients, 'distinctrates': distinctrates, 'distinctprices': distinctprices,
                           'navigationcontents': navigationcontents, 'restaurantcount': restaurantcount,
                           'marketcount': marketcount, })
        elif request.POST.get('hiddenTag'):
            hiddenTag = request.POST.get('hiddenTag')
            clients = SystemUser.objects.filter(is_client=True).filter(tags__tag__exact=hiddenTag).filter(
                tags_user_username_exact=request.user.username)
            restaurantcount = clients.filter(clientType='Restaurant').count()
            marketcount = clients.filter(clientType='Market').count()
            distinctrates = clients.values('clientrate').distinct().order_by('clientrate')
            distinctprices = clients.values('clientMinPrice').distinct().order_by('clientMinPrice')

            if request.user.is_authenticated:
                navigationcontents = NavigationContent.objects.filter(usertype='valid')
            else:
                navigationcontents = NavigationContent.objects.filter(usertype='visitor')
            return render(request, 'omosapp/restaurant.html',
                          {'clients': clients, 'distinctrates': distinctrates, 'distinctprices': distinctprices,
                           'navigationcontents': navigationcontents, 'restaurantcount': restaurantcount,
                           'marketcount': marketcount, })


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

        if request.user.is_authenticated:
            navigationcontents = NavigationContent.objects.filter(usertype='valid')
        else:
            navigationcontents = NavigationContent.objects.filter(usertype='visitor')
        return render(request, 'omosapp/myprofile.html',
                      {'myprofilecontents': myprofilecontents, 'navigationcontents': navigationcontents})
    else:
        myprofilecontents = MyProfileContent.objects.filter(usertype='none')
        if request.user.is_authenticated:
            navigationcontents = NavigationContent.objects.filter(usertype='valid')
        else:
            navigationcontents = NavigationContent.objects.filter(usertype='visitor')
        return render(request, 'omosapp/myprofile.html',
                      {'myprofilecontents': myprofilecontents, 'navigationcontents': navigationcontents})


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

    if request.user.is_authenticated:
        navigationcontents = NavigationContent.objects.filter(usertype='valid')
    else:
        navigationcontents = NavigationContent.objects.filter(usertype='visitor')
    return render(request, 'omosapp/login.html',
                  {'form': form, 'error_message': error_message, 'navigationcontents': navigationcontents, })


def exit_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            navigationcontents = NavigationContent.objects.filter(usertype='valid')
        else:
            navigationcontents = NavigationContent.objects.filter(usertype='visitor')
        return render(request, 'omosapp/exit.html', {'navigationcontents': navigationcontents, })
    else:
        if request.method == "POST" and 'leaveYes' in request.POST:
            logout(request)
            return redirect('home')
        else:
            return redirect('home')
