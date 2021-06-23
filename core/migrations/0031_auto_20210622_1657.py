# Generated by Django 3.1.2 on 2021-06-22 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20210620_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='category',
            field=models.ForeignKey(help_text='Select Category', on_delete=django.db.models.deletion.CASCADE, to='core.category'),
        ),
        migrations.AlterField(
            model_name='property',
            name='images_2',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]