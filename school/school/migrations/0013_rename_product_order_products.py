# Generated by Django 4.2 on 2023-05-15 14:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0012_order_product"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="product",
            new_name="products",
        ),
    ]
