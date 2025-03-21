# Generated by Django 5.1.5 on 2025-02-10 03:46

import markdownx.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0018_alter_blogpost_title_charset"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="content",
            field=markdownx.models.MarkdownxField(),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="featured_image",
            field=models.ImageField(blank=True, help_text="Featured image for the blog post", upload_to="blog/images/"),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="tags",
            field=models.CharField(
                blank=True, help_text="Comma-separated tags (e.g., 'python, django, web development')", max_length=200
            ),
        ),
    ]
