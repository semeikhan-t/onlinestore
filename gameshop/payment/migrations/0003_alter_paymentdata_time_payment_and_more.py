# Generated by Django 4.2.7 on 2024-02-29 06:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '0002_alter_paymentdata_time_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdata',
            name='time_payment',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 29, 12, 39, 10, 852445), verbose_name='Дата и время оплаты'),
        ),
        migrations.AlterField(
            model_name='paymentdata',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
