# Generated by Django 5.0.1 on 2024-10-09 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wsite", "0019_rename_description_productrating_comment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Classification",
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
                ("classify", models.CharField(default="nature", max_length=50)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "product_rating",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wsite.productrating",
                    ),
                ),
            ],
        ),
    ]