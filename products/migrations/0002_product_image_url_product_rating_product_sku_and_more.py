# Generated by Django 4.2.17 on 2024-12-12 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="rating",
            field=models.DecimalField(
                blank=True, decimal_places=1, max_digits=2, null=True
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="sku",
            field=models.CharField(default="SKU-DEFAULT", max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="products/"),
        ),
    ]
