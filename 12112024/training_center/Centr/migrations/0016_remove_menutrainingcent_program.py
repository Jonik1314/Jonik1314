# Generated by Django 3.2.25 on 2024-11-04 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Centr', '0015_menutrainingcent_program'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menutrainingcent',
            name='program',
        ),
    ]
