from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class DriverForm(forms.ModelForm):
    class Meta:
        model = Bus_Drivers
        fields = "__all__"


class BusForm(forms.ModelForm):

    class Meta:

        model = Bus
        fields = "__all__"


class LocationForm(forms.ModelForm):

    class Meta:

        model = Location
        fields = "__all__"


class routeForm(forms.Form):

    route_form = forms.IntegerField


class RouteLocationForm(forms.Form):

    model = ROUTE_LOCATION
    fields = "__all__"


class ScheduleForm(forms.ModelForm):

    class Meta:

        model = Bus_Driver_Route
        fields = "__all__"


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']