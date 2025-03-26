# Generated by Django 5.1.6 on 2025-03-26 04:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0044_waitingroom_fulfilled_course"),
    ]

    operations = [
        migrations.AddField(
            model_name="session",
            name="latitude",
            field=models.DecimalField(
                blank=True,
                decimal_places=6,
                help_text="Latitude coordinate for mapping",
                max_digits=9,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(-90),
                    django.core.validators.MaxValueValidator(90),
                ],
            ),
        ),
        migrations.AddField(
            model_name="session",
            name="longitude",
            field=models.DecimalField(
                blank=True,
                decimal_places=6,
                help_text="Longitude coordinate for mapping",
                max_digits=9,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(-180),
                    django.core.validators.MaxValueValidator(180),
                ],
            ),
        ),
        migrations.AddField(
            model_name="session",
            name="teaching_style",
            field=models.CharField(
                blank=True,
                choices=[
                    ("lecture", "Lecture Based"),
                    ("student-centered", "Student Centered"),
                    ("hybrid", "Hybrid Learning"),
                    ("practical", "Practical Learning"),
                ],
                default="hybrid",
                help_text="What is the teachng style of session",
                max_length=20,
            ),
        ),
    ]
