# Generated by Django 3.2.6 on 2021-09-13 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_profile_avt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_avt',
            field=models.ImageField(null=True, upload_to='images/avatar'),
        ),
    ]
