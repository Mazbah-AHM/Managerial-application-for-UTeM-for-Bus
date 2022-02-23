# Generated by Django 3.1.3 on 2020-12-16 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('Staff_Id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('Fname', models.CharField(max_length=25, null=True)),
                ('Lname', models.CharField(max_length=25, null=True)),
                ('Email', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bus_Driver_Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bus_Driver_Id', models.CharField(max_length=15)),
                ('Date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('Reservation_Id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('Student_Id', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ROUTE',
            fields=[
                ('Route_Id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ROUTE_LOCATION',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Student_Id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('Fname', models.CharField(max_length=25, null=True)),
                ('Lname', models.CharField(max_length=25, null=True)),
                ('Email', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='bus',
            name='Capacity',
        ),
        migrations.AlterField(
            model_name='bus',
            name='Bus_Driver_Id',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='Location_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]