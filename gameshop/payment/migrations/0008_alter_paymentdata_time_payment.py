# Generated by Django 4.2.7 on 2023-12-25 14:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0007_rename_payment_date_paymentdata_time_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdata',
            name='time_payment',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 25, 20, 1, 34, 978802), verbose_name='Дата и время оплаты'),
        ),
    ]
