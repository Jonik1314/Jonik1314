# Generated by Django 3.2.25 on 2024-10-11 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Centr', '0002_menuabout'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuabout',
            name='type',
            field=models.CharField(choices=[('OsS', 'Основные сведенения'),
                                            ('Dok', 'Документы'),
                                            ('Obr', 'Образование'),
                                            ('POU', 'Платные образовательные услуги')],
                                   default='OsS', max_length=3, verbose_name='Тип'),
        ),
    ]
