# Generated by Django 3.2.1 on 2021-06-14 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='currency',
            field=models.CharField(max_length=10, null=True),
        ),
    ]