# Generated by Django 3.0.5 on 2020-11-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20201127_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'User'), ('moderator', 'Moderator'), ('admin', 'Admin')], default='user', max_length=20),
        ),
    ]