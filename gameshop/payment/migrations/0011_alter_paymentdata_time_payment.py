# Generated by Django 4.2.7 on 2023-12-27 12:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0010_alter_paymentdata_time_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdata',
            name='time_payment',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 27, 18, 3, 6, 970315), verbose_name='Дата и время оплаты'),
        ),
    ]