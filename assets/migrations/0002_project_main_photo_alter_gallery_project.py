# Generated by Django 5.0.2 on 2024-02-20 02:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("assets", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="main_photo",
            field=models.ImageField(default=1, upload_to="project_photos/"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="gallery",
            name="project",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="project_images",
                to="assets.project",
            ),
        ),
    ]