# Generated by Django 4.2.7 on 2023-12-27 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_productcategory_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
