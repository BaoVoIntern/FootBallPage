# Generated by Django 3.2.6 on 2021-09-13 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_account_profile_avt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_avt',
            field=models.ImageField(blank=True, null=True, upload_to='images/avatar'),
        ),
    ]
