# Generated by Django 3.0.5 on 2020-11-13 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_merge_20201113_1259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='confirmations_code',
            new_name='confirmation_code',
        ),
    ]
