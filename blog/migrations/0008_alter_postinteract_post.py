# Generated by Django 3.2.5 on 2021-08-20 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_postinteract_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postinteract',
            name='post',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
    ]
