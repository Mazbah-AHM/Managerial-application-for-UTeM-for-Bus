# Generated by Django 3.1.3 on 2021-01-20 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0043_auto_20210120_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus_drivers',
            name='Email',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='bus_drivers',
            name='Fname',
            field=models.TextField(max_length=25),
        ),
        migrations.AlterField(
            model_name='bus_drivers',
            name='Lname',
            field=models.TextField(max_length=25),
        ),
    ]
