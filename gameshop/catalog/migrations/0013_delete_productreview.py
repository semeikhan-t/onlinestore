# Generated by Django 4.2.7 on 2024-03-19 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_alter_productreview_product_alter_productreview_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductReview',
        ),
    ]
