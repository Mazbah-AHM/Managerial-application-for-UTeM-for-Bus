from django.db import models

# Create your models here.


class Bus_Drivers(models.Model):

    Bus_Driver_id = models.AutoField(primary_key=True)
    Fname = models.TextField(max_length=25, blank=False)
    Lname = models.TextField(max_length=25, blank=False)
    Email = models.CharField(max_length=50, default=None)
    Contact_Number = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.Fname


class Bus(models.Model):
    Bus_id = models.CharField(max_length=10, primary_key=True)
    Capacity = models.IntegerField(null=True)
    Bus_Driver = models.ForeignKey(
        Bus_Drivers, on_delete=models.CASCADE, default=None)


class Location(models.Model):

    Location_id = models.AutoField(primary_key=True)
    Location_Name = models.CharField(max_length=100, null=True)
    Latitude = models.DecimalField(max_digits=25, decimal_places=20)
    Longtitude = models.DecimalField(max_digits=25, decimal_places=20)

    def __int__(self):
        return self.Location_id


class ROUTE (models.Model):

    Route_id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.Route_id)


class Student(models.Model):

    Student_id = models.CharField(primary_key=True,max_length = 15)
    Fname = models.CharField(max_length=25, null=True)
    Lname = models.CharField(max_length=25, null=True)
    Email = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.Student_id


class Admin(models.Model):

    username = models.IntegerField(primary_key=True)
    Fname = models.CharField(max_length=25, null=True)
    Lname = models.CharField(max_length=25, null=True)
    Email = models.EmailField(max_length=50, null=True)
    password = models.CharField(max_length=32,default=None)

    def __str__(self):
        return self.Fname


class Reservation(models.Model):

    Reservation_id = models.IntegerField(primary_key=True)
    Student = models.ForeignKey(
        Student, on_delete=models.CASCADE, default=None)
    Route = models.ForeignKey(ROUTE, on_delete=models.CASCADE, default=None)
    Bus_Driver_Route_id = models.IntegerField(null=True)
    From_Location_id = models.IntegerField(null=True)
    To_Location_id = models.IntegerField(null=True)
    Departure_Time = models.TimeField(null=True)
    Arrival_Time = models.TimeField(null=True)
    Date = models.DateField(null=True)
    Status = models.IntegerField(null=True, default=0)

    def __int__(self):
        return self.Reservation_id


class Bus_Driver_Route(models.Model):

    Bus_Driver_Route_id = models.AutoField(primary_key=True)
    Bus_Driver = models.ForeignKey(Bus_Drivers, on_delete=models.CASCADE, default=None)
    Route = models.ForeignKey(ROUTE, on_delete=models.CASCADE, default=None)
    Date = models.DateField(null=True)
    Departure_Time = models.TimeField(null=True)
    Status = models.IntegerField(null=True)




class ROUTE_LOCATION(models.Model):

    Route_Location_id = models.AutoField(primary_key=True)
    Route = models.ForeignKey(ROUTE, on_delete=models.CASCADE, default=None)
    Location = models.ForeignKey(
        Location, on_delete=models.PROTECT, default=None)
    Location_Order = models.IntegerField(null=True)
    Estimated_Time = models.TimeField(null=True)
