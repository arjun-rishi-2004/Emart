# Generated by Django 4.2 on 2023-04-11 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0004_alter_cart_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='date_created',
        ),
    ]
