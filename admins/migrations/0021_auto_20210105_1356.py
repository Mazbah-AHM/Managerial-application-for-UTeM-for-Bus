# Generated by Django 3.1.3 on 2021-01-05 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0020_admin_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='Staff_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]