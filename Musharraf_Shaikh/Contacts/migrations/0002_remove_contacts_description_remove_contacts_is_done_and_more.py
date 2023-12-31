# Generated by Django 5.0 on 2023-12-05 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='description',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='is_done',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='notes',
        ),
        migrations.AddField(
            model_name='contacts',
            name='phone_number',
            field=models.CharField(default='null', max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
