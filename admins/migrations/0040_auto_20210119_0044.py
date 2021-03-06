# Generated by Django 3.1.3 on 2021-01-19 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0039_auto_20210118_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus_driver_route',
            name='Current_Latitude',
            field=models.DecimalField(decimal_places=7, default=2.313796, max_digits=10),
        ),
        migrations.AddField(
            model_name='bus_driver_route',
            name='Current_Longtitude',
            field=models.DecimalField(decimal_places=7, default=102.321077, max_digits=10),
        ),
    ]
