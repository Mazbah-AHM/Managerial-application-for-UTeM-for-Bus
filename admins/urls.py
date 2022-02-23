from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.Home, name=""),

    path('register/', views.RegistrationPage, name="register"),
    path('login/', views.LoginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('createbus/', views.createBus, name="createbus"),
    path('updatebus/<str:id>', views.updateBus, name="updatebus"),
    path('editbus/<str:id>', views.editBus, name="editbus"),
    path('deletebus/<str:id>', views.deleteBus, name="deletebus"),
    path('showbus/', views.showBus, name="showbus"),

    path('createdriver/', views.createDriver, name="createdriver"),
    path('updatedriver/<int:id>', views.updateDriver, name="updatedriver"),
    path('editdriver/<int:id>', views.editDriver, name="editdriver"),
    path('deletedriver/<int:id>', views.deleteDriver, name="deletedriver"),
    path('showdriver/', views.showDriver, name="showdriver"),

    path('addschedule/', views.addSchedule, name="addschedule"),
    path('updateschedule/<int:id>', views.updateSchedule, name="updateschedule"),
    path('editschedule/<int:id>', views.editDriver, name="editschedule"),
    path('deleteschedule/<int:id>', views.deleteSchedule, name="deleteschedule"),
    path('showschedule/', views.showSchedule, name="showschedule"),
    path('showrouteloc/', views.showRouteLocation, name="showrouteloc"),

    path('addlocation/', views.addLocation, name="addlocation"),
    path('showlocation/', views.showLocation, name="showlocation"),
    path('deletelocation/<int:id>', views.deleteLocation, name="deletelocation"),

    path('addroute/', views.addRoute, name="addroute"),
    path('showroute/', views.showRoute, name="showroute"),
    path('deleteroute/<int:id>', views.deleteRoute, name="deleteroute"),
    path('route_location/', views.routeLocation, name="route_location"),
    path('deleterouteloc/<int:id>', views.deleteRouteloc, name="deleterouteloc"),

    path('reservation/', views.Reservations, name="reservation"),
    path('deletereservation/<int:id>', views.deleteReservation, name="deletereservation"),

    path('reset_password/', 
    auth_views.PasswordResetView.as_view(template_name="admins/password_reset.html"), 
    name = "reset_password"),

    path('reset_password_sent/', 
    auth_views.PasswordResetDoneView.as_view(template_name="admins/password_reset_sent.html"), 
    name = "password_reset_done"),

    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name="admins/password_reset_form.html"), 
    name="password_reset_confirm"),
    
    path('reset_password_complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name="admins/password_reset_done.html"), 
    name = "password_reset_complete"),

]
