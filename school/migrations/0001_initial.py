# Generated by Django 4.1 on 2024-08-28 13:35

import common.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("assets", "0001_initial"),
        ("production", "0001_initial"),
        ("people", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Promotion",
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
                ("name", models.CharField(max_length=255)),
                ("starting_year", models.PositiveSmallIntegerField()),
                ("ending_year", models.PositiveSmallIntegerField()),
                (
                    "picture",
                    models.ImageField(blank=True, upload_to=common.utils.make_filepath),
                ),
            ],
            options={
                "ordering": ["starting_year"],
            },
        ),
        migrations.CreateModel(
            name="VisitingStudent",
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
                ("number", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "artist",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="visiting_student",
                        to="people.artist",
                    ),
                ),
                (
                    "promotion",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="school.promotion",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["artist"],
            },
        ),
        migrations.CreateModel(
            name="TeachingArtist",
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
                (
                    "presentation_text_fr",
                    models.TextField(
                        blank=True,
                        help_text="General orientation text (not only bio) in FRENCH",
                        null=True,
                    ),
                ),
                (
                    "presentation_text_en",
                    models.TextField(
                        blank=True,
                        help_text="General orientation text (not only bio) in ENGLISH",
                        null=True,
                    ),
                ),
                (
                    "artist",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="teacher",
                        to="people.artist",
                    ),
                ),
                (
                    "artworks_supervision",
                    models.ManyToManyField(
                        blank=True, related_name="mentoring", to="production.artwork"
                    ),
                ),
                (
                    "pictures_gallery",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="teachingartist_pictures",
                        to="assets.gallery",
                    ),
                ),
            ],
            options={
                "ordering": ["artist"],
            },
        ),
        migrations.CreateModel(
            name="Student",
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
                ("number", models.CharField(blank=True, max_length=50, null=True)),
                ("graduate", models.BooleanField(default=False)),
                (
                    "diploma_mention",
                    models.CharField(
                        blank=True,
                        help_text="Diploma mention",
                        max_length=150,
                        null=True,
                    ),
                ),
                (
                    "artist",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="student",
                        to="people.artist",
                    ),
                ),
                (
                    "promotion",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="school.promotion",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["artist__user__first_name"],
            },
        ),
        migrations.CreateModel(
            name="ScienceStudent",
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
                ("field", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "student",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="science_student",
                        to="school.student",
                    ),
                ),
            ],
            options={
                "ordering": ["student"],
            },
        ),
        migrations.CreateModel(
            name="PhdStudent",
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
                (
                    "thesis_object",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "thesis_file",
                    models.FileField(
                        blank=True,
                        help_text="thesis pdf file",
                        null=True,
                        upload_to=common.utils.make_filepath,
                    ),
                ),
                (
                    "directors",
                    models.ManyToManyField(
                        blank=True,
                        related_name="phd_student",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "student",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="phd_student",
                        to="school.student",
                    ),
                ),
                (
                    "university",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="phd_student",
                        to="people.organization",
                    ),
                ),
            ],
            options={
                "ordering": ["student"],
            },
        ),
    ]
