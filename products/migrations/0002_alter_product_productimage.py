# Generated by Django 4.0.4 on 2022-05-08 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productImage',
            field=models.ImageField(default='media/productPic.jpg', null=True, upload_to='photos/%y/%m/%d'),
        ),
    ]
