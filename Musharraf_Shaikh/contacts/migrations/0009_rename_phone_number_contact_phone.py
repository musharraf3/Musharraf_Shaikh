# Generated by Django 5.0 on 2023-12-06 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0008_alter_contact_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='phone_number',
            new_name='phone',
        ),
    ]
