# Generated by Django 5.0.2 on 2024-02-24 09:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_alter_blog_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomeGallery",
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
                ("title", models.CharField(max_length=200)),
                ("image", models.ImageField(upload_to="homegallery/")),
            ],
        ),
    ]
