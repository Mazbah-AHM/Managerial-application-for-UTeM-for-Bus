# Generated by Django 3.1.3 on 2020-12-23 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0010_auto_20201223_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='Capacity',
            field=models.IntegerField(null=True),
        ),
    ]
