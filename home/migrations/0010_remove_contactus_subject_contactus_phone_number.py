# Generated by Django 5.0.2 on 2024-02-26 15:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0009_aboutus_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contactus",
            name="subject",
        ),
        migrations.AddField(
            model_name="contactus",
            name="phone_number",
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
