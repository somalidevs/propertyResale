# Generated by Django 3.1.2 on 2021-07-06 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_subscription_stripe_price_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='stripe_price_id',
        ),
        migrations.AddField(
            model_name='plan',
            name='stripe_price_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]