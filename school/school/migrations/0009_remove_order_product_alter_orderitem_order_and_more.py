# Generated by Django 4.2 on 2023-04-30 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0008_alter_order_transaction_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="product",
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="order",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="school.order",
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="school.product"
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="quantity",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="product",
            field=models.ManyToManyField(
                through="school.OrderItem", to="school.product"
            ),
        ),
    ]
