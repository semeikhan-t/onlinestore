# Generated by Django 4.2.7 on 2023-12-15 10:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_alter_paymentdata_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdata',
            name='card_number',
            field=models.PositiveIntegerField(max_length=16, validators=[django.core.validators.MinValueValidator(16), django.core.validators.MaxValueValidator(16)], verbose_name='Номер карты'),
        ),
        migrations.AlterField(
            model_name='paymentdata',
            name='cvv',
            field=models.CharField(max_length=3, validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(3)], verbose_name='CVV'),
        ),
        migrations.AlterField(
            model_name='paymentdata',
            name='post_index',
            field=models.CharField(max_length=5, validators=[django.core.validators.MinValueValidator(10000), django.core.validators.MaxValueValidator(99999)], verbose_name='Почтовый индекс'),
        ),
    ]
