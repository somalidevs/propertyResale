# Generated by Django 3.1.2 on 2021-07-15 17:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_remove_property_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]