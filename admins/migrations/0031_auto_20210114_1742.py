# Generated by Django 3.1.3 on 2021-01-14 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0030_auto_20210114_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='Route_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
