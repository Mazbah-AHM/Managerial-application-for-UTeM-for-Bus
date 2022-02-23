from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from django.contrib import messages

from .forms import *
from.models import *

# Create your views here.

@login_required(login_url='login')
def Home(request):

    reservation = Reservation.objects.all()

    context = {'reservebus': reservation}

    return render(request, 'admins/dashboard.html', context)



def RegistrationPage(request):
    if request.user.is_authenticated:
        return redirect('')
    else:        
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():            
                form.save()
                return redirect('login')
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was succesfully created for' + user)

        context = {'form':form}           
        return render(request,'admins/register.html', context) 



def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('')
            else:
                messages.error(request, 'Invalid username or password!')    

        
        context = {}

        return render(request,'admins/login.html', context)      


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def createBus(request):

    bdid = Bus_Drivers.objects.all()
    if request.method == "POST":
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showbus')
    else:
        form = BusForm()

    return render(request, 'admins/createbus.html', {'form': form, 'bd': bdid})

@login_required(login_url='login')
def updateBus(request, id):

    bdid = Bus_Drivers.objects.all()
    update = Bus.objects.get(Bus_id=id)
    form = BusForm(request.POST, instance=update)
    if form.is_valid():
        form.save()
        return redirect('showbus')

    return render(request, 'admins/updatebus.html', {'update': update, 'bdi': bdid})

@login_required(login_url='login')
def editBus(request, id):

    update = Bus.objects.get(Bus_id=id)

    context = {'update': update}

    return render(request, 'admins/updatebus.html', context)

@login_required(login_url='login')
def deleteBus(request, id):

    remove = Bus.objects.get(Bus_id=id)
    remove.delete()

    return redirect('showbus')

@login_required(login_url='login')
def showBus(request):
    showbus = Bus.objects.all()

    context = {'buslist': showbus}
    return render(request, 'admins/showbus.html', context)

@login_required(login_url='login')
def createDriver(request):

    if request.method == "POST":
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return showDriver(request)
    else:
        form = DriverForm()

    context = {'form': form}
    return render(request, 'admins/createdriver.html', context)

@login_required(login_url='login')
def updateDriver(request, id):

    update = Bus_Drivers.objects.get(Bus_Driver_id=id)
    form = DriverForm(request.POST, instance=update)
    if form.is_valid():
        form.save()
        return redirect('showdriver')

    context = {'update': update}
    return render(request, 'admins/updatedriver.html', context)

@login_required(login_url='login')
def editDriver(request, id):

    update = Bus_Drivers.objects.get(Bus_Driver_id=id)

    context = {'update': update}

    return render(request, 'admins/updatedriver.html', context)

@login_required(login_url='login')
def deleteDriver(request, id):

    remove = Bus_Drivers.objects.get(Bus_Driver_id=id)
    remove.delete()

    return redirect('showdriver')

@login_required(login_url='login')
def showDriver(request):
    showdriver = Bus_Drivers.objects.all()

    context = {'driverlist': showdriver}
    return render(request, 'admins/showdriver.html', context)

@login_required(login_url='login')
def addSchedule(request):

    showway = ROUTE.objects.all()
    showrider = Bus_Drivers.objects.all()

    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():

            print('valid')
            form.save()
            return redirect('showschedule')
    else:
        form = ScheduleForm()
    print(form.errors)
    print('not valid')
    return render(request, 'admins/addschedule.html', {'form': form, 'sw': showway, 'sr': showrider})

@login_required(login_url='login')
def updateSchedule(request, id):

    showway = ROUTE.objects.all()
    showrider = Bus_Drivers.objects.all()
    update = Bus_Driver_Route.objects.get(Bus_Driver_Route_id=id)
    form = ScheduleForm(request.POST, instance=update)
    if form.is_valid():
        form.save()
        return redirect('showschedule')

    return render(request, 'admins/updateschedule.html', {'update': update, 'sw': showway, 'sr': showrider})

@login_required(login_url='login')
def editSchedule(request, id):

    update = Bus_Driver_Route.objects.get(Bus_Driver_Route_id=id)

    return render(request, 'admins/updateschedule.html', {'update': update})

@login_required(login_url='login')
def deleteSchedule(request, id):

    remove = Bus_Driver_Route.objects.get(Bus_Driver_Route_id=id)
    remove.delete()

    return redirect('showschedule')

@login_required(login_url='login')
def showSchedule(request):

    showsche = Bus_Driver_Route.objects.all()
    context = {'shows': showsche}
    return render(request, 'admins/showschedule.html', context)

@login_required(login_url='login')
def addLocation(request):

    form = LocationForm()
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return showLocation(request)

    context = {'form': form}

    return render(request, 'admins/addlocation.html', context)

@login_required(login_url='login')
def showLocation(request):

    showloc = Location.objects.all()
    context = {'showlocation': showloc}

    return render(request, 'admins/showlocation.html', context)

@login_required(login_url='login')
def deleteLocation(request, id):

    remove = Location.objects.get(Location_id=id)
    remove.delete()
    return redirect('showlocation')

@login_required(login_url='login')
def addRoute(request):
    showloc = Location.objects.all()
    print(showloc)
    if request.method == 'POST':

        form = routeForm(request.POST)
        if form.is_valid():

            return render(request, 'admins/route_location.html', {'n': range(int(form.data['val'])), 'showLoc': showloc})

    context = {}
    return render(request, 'admins/addroute.html', context)

@login_required(login_url='login')
def showRoute(request):

    showrout = ROUTE.objects.all()
    context = {'showroute': showrout}

    return render(request, 'admins/showroute.html', context)

@login_required(login_url='login')
def deleteRoute(request, id):

    remove = ROUTE.objects.get(Route_id=id)
    remove.delete()
    return redirect('showroute')


@login_required(login_url='login')
def Reservations(request):

    reservation = Reservation.objects.all()

    context = {'reservebus': reservation}

    return render(request, 'admins/reservations.html', context)

@login_required(login_url='login')
def deleteReservation(request, id):

    remove = Reservation.objects.get(Reservation_id=id)
    remove.delete()
    return redirect('reservation')        


@login_required(login_url='login')
def routeLocation(request):

    if request.method == 'POST':

        locations = request.POST.getlist('Location')
        locationOrders = request.POST.getlist('Location_Order')
        estTimes = request.POST.getlist('Estimated_Time')

        rou = ROUTE()
        rid = rou.save()
        print(rou.Route_id)

        for (i, j, k) in zip(locations, locationOrders, estTimes):
            rouloc = ROUTE_LOCATION(
                Route_id=rou.Route_id,
                Location_id=i,
                Location_Order=j,
                Estimated_Time=k
            )
            rouloc.save()

    return redirect('showrouteloc')

@login_required(login_url='login')
def showRouteLocation(request):

    showroutloc = ROUTE_LOCATION.objects.all()
    showloc = Location.objects.all()
    context = {'showrouteloc': showroutloc, 'shol':showloc}

    return render(request, 'admins/showrouteloc.html', context)

@login_required(login_url='login')
def deleteRouteloc(request, id):

    remove = ROUTE_LOCATION.objects.get(Route_Location_id=id)
    remove.delete()
    return redirect('showrouteloc')    