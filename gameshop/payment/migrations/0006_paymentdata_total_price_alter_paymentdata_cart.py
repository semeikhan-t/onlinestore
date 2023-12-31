# Generated by Django 4.2.7 on 2023-12-19 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_paymentdata_cart_alter_paymentdata_cardholder_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentdata',
            name='total_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Итоговая цена'),
        ),
        migrations.AlterField(
            model_name='paymentdata',
            name='cart',
            field=models.JSONField(null=True, verbose_name='Товары'),
        ),
    ]
