# Generated by Django 5.0.2 on 2024-02-16 02:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="property",
            name="availability",
            field=models.CharField(
                choices=[
                    ("sold_out", "SOLD OUT"),
                    ("for_rent", "For Rent"),
                    ("for_sale", "For Sale"),
                    ("available", "Available"),
                ],
                default="available",
                max_length=20,
            ),
        ),
    ]
