# Generated by Django 2.1.7 on 2020-07-06 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='is_admin',
            new_name='is_staff',
        ),
    ]
