# Generated by Django 3.1.3 on 2021-01-05 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0019_auto_20210102_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='Password',
            field=models.CharField(default=None, max_length=32),
        ),
    ]
