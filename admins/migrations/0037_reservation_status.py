# Generated by Django 3.1.3 on 2021-01-18 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0036_auto_20210114_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='Status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
