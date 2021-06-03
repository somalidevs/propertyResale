# Generated by Django 3.2.1 on 2021-05-30 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_customer_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]