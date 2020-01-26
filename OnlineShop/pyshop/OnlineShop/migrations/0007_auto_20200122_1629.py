# Generated by Django 3.0.1 on 2020-01-22 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineShop', '0006_item_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
