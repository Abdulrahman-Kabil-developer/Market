# Generated by Django 4.0.4 on 2022-05-28 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_productseller'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='soldStatus',
            field=models.BooleanField(default=False),
        ),
    ]