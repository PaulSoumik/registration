# Generated by Django 2.1.7 on 2020-07-06 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20200706_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='varification_id',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='varified',
        ),
    ]
