# Generated by Django 3.1.3 on 2020-12-26 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0014_auto_20201225_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='Staff_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bus',
            name='Bus_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bus_driver_route',
            name='Bus_Driver_Route_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='location',
            name='Location_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='Reservation_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='route_location',
            name='Route_Location_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='Student_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]