# Generated by Django 5.0 on 2023-12-06 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_rename_contacts_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(default='+1', max_length=12, unique=True),
        ),
    ]
