# Generated by Django 4.1 on 2022-08-24 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0002_snack_create'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snack',
            old_name='create',
            new_name='created',
        ),
    ]
