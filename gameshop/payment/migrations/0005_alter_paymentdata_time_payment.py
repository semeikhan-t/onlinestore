# Generated by Django 4.2.7 on 2024-03-17 11:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_alter_paymentdata_time_payment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdata',
            name='time_payment',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 17, 16, 48, 38, 388302), verbose_name='Дата и время оплаты'),
        ),
    ]
