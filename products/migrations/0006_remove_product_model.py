# Generated by Django 4.2.17 on 2024-12-12 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0005_product_model"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="model",
        ),
    ]
