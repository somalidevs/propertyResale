# Generated by Django 3.2.1 on 2021-05-31 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210531_0706'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='plan_list1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='plan_list2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]