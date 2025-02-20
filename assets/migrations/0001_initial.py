# Generated by Django 4.1 on 2024-08-28 13:35

import common.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Gallery",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("updated_on", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name_plural": "galleries",
            },
        ),
        migrations.CreateModel(
            name="Medium",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("position", models.PositiveIntegerField(default=1)),
                ("label", models.CharField(blank=True, max_length=255, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "picture",
                    models.ImageField(
                        blank=True, null=True, upload_to=common.utils.make_filepath
                    ),
                ),
                ("medium_url", models.URLField(blank=True, null=True)),
                (
                    "file",
                    models.FileField(
                        blank=True, null=True, upload_to=common.utils.make_filepath
                    ),
                ),
                (
                    "gallery",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="media",
                        to="assets.gallery",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "media",
                "ordering": ("position",),
            },
        ),
    ]
