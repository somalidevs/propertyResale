# Generated by Django 3.1.2 on 2021-06-23 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_enquiry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enquiry',
            old_name='Message',
            new_name='message',
        ),
    ]