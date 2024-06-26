# Generated by Django 4.2.7 on 2024-02-09 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_remove_product_cat_product_cat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id'], 'verbose_name': 'Карточка товара', 'verbose_name_plural': 'Карточки товаров'},
        ),
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.ManyToManyField(to='catalog.productcategory', verbose_name='Категория'),
        ),
    ]
