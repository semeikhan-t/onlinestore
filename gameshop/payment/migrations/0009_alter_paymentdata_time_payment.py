# Generated by Django 4.2.7 on 2023-12-25 14:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0008_alter_paymentdata_time_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdata',
            name='time_payment',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 25, 20, 2, 32, 665117), verbose_name='Дата и время оплаты'),
        ),
    ]
