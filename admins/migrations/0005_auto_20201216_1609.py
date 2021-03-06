# Generated by Django 3.1.3 on 2020-12-16 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0004_auto_20201216_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus_driver_route',
            name='Route_Id',
        ),
        migrations.AddField(
            model_name='bus_driver_route',
            name='Route_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='admins.route'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='route',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='admins.route'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='Student_Id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='admins.student'),
        ),
    ]
