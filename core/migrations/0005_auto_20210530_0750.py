# Generated by Django 3.2.1 on 2021-05-30 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210530_0748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='property',
            name='slug',
        ),
    ]
