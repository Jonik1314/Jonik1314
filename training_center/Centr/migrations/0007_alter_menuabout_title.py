# Generated by Django 3.2.25 on 2024-10-11 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Centr', '0006_alter_menuabout_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuabout',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
    ]
