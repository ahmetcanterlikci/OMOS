from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.utils import timezone

from omosapp.forms import LoginUser
from omosapp.models import SystemUser, NavigationContent, MyProfileContent, ClientCategory, Chart, Order


def home(request):
    if request.user.is_authenticated:
        navigationcontents = NavigationContent.objects.filter(usertype='valid')
    else:
        navigationcontents = NavigationContent.objects.filter(usertype='visitor')
    return render(request, 'omosapp/index.html', {'navigationcontents': navigationcontents})


def base_view(request):
    return render(request, 'omosapp/base.html', {})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view')
    else:
        form = form = UserCreationForm()
        return render(request, 'omosapp/register.html', {'form': form, })


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

        if request.user.is_authenticated:
            navigationcontents = NavigationContent.objects.filter(usertype='valid')
        else:
            navigationcontents = NavigationContent.objects.filter(usertype='visitor')
        return render(request, 'omosapp/changePassword.html',
                      {'changepasswordform': changepasswordform, 'navigationcontents': navigationcontents, })


def chart(request):
    if request.method == "POST":

        if request.POST.get('cancel'):
            itemName = request.POST.get('itemName')
            clientusername = request.POST.get('clientName')
            selecteditem = Chart.objects.filter(customer__username__exact=request.user.username).filter(
                itemName__exact=itemName).filter(clientName__exact=clientusername).delete()
            return redirect('chart')
        else:
            itemName = request.POST.get('itemName')
            itemPrice = request.POST.get('itemPrice')
            itemcount = request.POST.get('itemcount')
            clientusername = request.POST.get('clientName')
            userprofile = SystemUser.objects.filter(user__username__exact=clientusername).get()

            newchart = Chart(customer=request.user, clientName=clientusername, itemName=itemName, itemPrice=itemPrice,
                             itemCount=itemcount, clientNameText=userprofile.clientName)
            newchart.save()
            return redirect('chart')

    else:
        charts = Chart.objects.filter(customer__username__exact=request.user.username)
        totalPrice = 0.00
        for chart in charts:
            totalPrice = float(chart.itemPrice) + totalPrice

        if request.user.is_authenticated:
            navigationcontents = NavigationContent.objects.filter(usertype='valid')
        else:
            navigationcontents = NavigationContent.objects.filter(usertype='visitor')

        return render(request, 'omosapp/chart.html',
                      {'charts': charts, 'totalPrice': totalPrice, 'navigationcontents': navigationcontents, })


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
                       'navigationcontents': navigationcontents, 'restaurantcount': restaurantcount,
                       'marketcount': marketcount, })
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
            print(hiddenTag)
            clients = SystemUser.objects.filter(is_client=True).filter(clientTags__icontains=hiddenTag)
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
        else:
            return redirect('search')


def myclients(request):
    return render(request, 'omosapp/myclients.html', {})


def myorders(request):
    distinctorderNumbers = Order.objects.values('orderNumber').distinct()

    orderlistActive = []
    orderlistCompleted = []
    orderlistCancelled = []

    for orderitem in distinctorderNumbers:
        selectedorders = Order.objects.filter(orderNumber__exact=orderitem['orderNumber'])
        for order2 in selectedorders:
            if order2.status == 'Active':
                orderlistActive.append(selectedorders)
                break
            elif order2.status == 'Completed':
                orderlistCompleted.append(selectedorders)
                break
            elif order2.status == 'Cancelled':
                orderlistCancelled.append(selectedorders)
                break

    if request.user.is_authenticated:
        navigationcontents = NavigationContent.objects.filter(usertype='valid')
    else:
        navigationcontents = NavigationContent.objects.filter(usertype='visitor')

    return render(request, 'omosapp/myorders.html',
                  {'orderlistActive': orderlistActive, 'orderlistCompleted': orderlistCompleted,
                   'orderlistCancelled': orderlistCancelled, 'navigationcontents': navigationcontents, })


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
    if request.method == "GET":
        return redirect('search')
    else:
        clientusername = request.POST.get('clientusername')
        client = SystemUser.objects.filter(user__username__exact=clientusername)
        clientcats = ClientCategory.objects.filter(user__username__exact=clientusername)

        if request.user.is_authenticated:
            navigationcontents = NavigationContent.objects.filter(usertype='valid')
        else:
            navigationcontents = NavigationContent.objects.filter(usertype='visitor')
        return render(request, 'omosapp/order.html',
                      {'clientcats': clientcats, 'client': client, 'navigationcontents': navigationcontents, })


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


def checkout(request):
    user = request.user
    userprofile = SystemUser.objects.filter(user__username__exact=request.user.username).get()
    chartitems = Chart.objects.filter(customer__username__exact=request.user.username)

    totalPrice = 0.00
    for chart in chartitems:
        totalPrice = float(chart.itemPrice) + totalPrice

    if request.user.is_authenticated:
        navigationcontents = NavigationContent.objects.filter(usertype='valid')
    else:
        navigationcontents = NavigationContent.objects.filter(usertype='visitor')
    return render(request, 'omosapp/checkout.html',
                  {'user': user, 'userprofile': userprofile, 'chartitems': chartitems, 'totalprice': totalPrice,
                   'navigationcontents': navigationcontents, })


def ordersuccess(request):
    if request.method == "POST":
        chartitems = Chart.objects.filter(customer__username__exact=request.user.username)
        userprofile = SystemUser.objects.filter(user__username__exact=request.user.username).get()

        totalPrice = 0.00
        for chart in chartitems:
            totalPrice = float(chart.itemPrice) + totalPrice

        orderNumber = "SIP"
        for chartitem in chartitems:
            orderNumber = orderNumber + str(chartitem.id)

        for chartitem in chartitems:
            neworder = Order(customer=request.user, clientUsername=chartitem.clientName, itemName=chartitem.itemName,
                             itemPrice=chartitem.itemPrice, itemCount=chartitem.itemCount, status='Active',
                             clientName=chartitem.clientNameText, orderNumber=orderNumber, clientAddress=userprofile.address)
            neworder.save()

        for chartitem in chartitems:
            chartitem.delete()

        if request.user.is_authenticated:
            navigationcontents = NavigationContent.objects.filter(usertype='valid')
        else:
            navigationcontents = NavigationContent.objects.filter(usertype='visitor')
        return render(request, 'omosapp/ordersuccess.html',
                      {'orderNumber': orderNumber, 'navigationcontents': navigationcontents, })

    else:
        return redirect('home')
