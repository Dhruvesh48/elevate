# Generated by Django 4.2.17 on 2024-12-16 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0003_alter_order_country"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderlineitem",
            name="product_size",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
