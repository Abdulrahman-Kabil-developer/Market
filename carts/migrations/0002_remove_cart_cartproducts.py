# Generated by Django 4.0.4 on 2022-05-17 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cartProducts',
        ),
    ]