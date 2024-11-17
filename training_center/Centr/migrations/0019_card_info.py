# Generated by Django 3.2.25 on 2024-11-04 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Centr', '0018_alter_more_detailed_kurs'),
    ]

    operations = [
        migrations.CreateModel(
            name='card_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Дата')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('type', models.CharField(choices=[('DPD', 'Доподготовка'), ('PPD', 'Переподготовка')], default='PPD', max_length=3, verbose_name='Тип')),
                ('format_learning', models.CharField(max_length=200, verbose_name='Формат обучения')),
                ('duration', models.CharField(max_length=50, verbose_name='Продолжительность курса')),
                ('program_volume', models.CharField(max_length=100, verbose_name='Объем программы')),
                ('requirements', models.TextField(verbose_name='Требования')),
            ],
        ),
    ]