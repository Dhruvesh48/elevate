# Generated by Django 4.2.17 on 2024-12-11 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="profile_pictures/"
                    ),
                ),
                ("fitness_goal", models.TextField(blank=True, null=True)),
                ("dietary_preference", models.TextField(blank=True, null=True)),
                (
                    "subscription_status",
                    models.CharField(
                        choices=[("ACTIVE", "Active"), ("INACTIVE", "Inactive")],
                        default="INACTIVE",
                        max_length=20,
                    ),
                ),
                ("renewal_date", models.DateField(blank=True, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
