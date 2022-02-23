# Generated by Django 3.1.3 on 2021-01-20 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0044_auto_20210120_0504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus_driver_route',
            name='Current_Latitude',
        ),
        migrations.RemoveField(
            model_name='bus_driver_route',
            name='Current_Longtitude',
        ),
        migrations.AlterField(
            model_name='location',
            name='Latitude',
            field=models.DecimalField(decimal_places=20, max_digits=25),
        ),
        migrations.AlterField(
            model_name='location',
            name='Location_Name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='Longtitude',
            field=models.DecimalField(decimal_places=20, max_digits=25),
        ),
    ]
