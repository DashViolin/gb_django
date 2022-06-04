# Generated by Django 3.2.13 on 2022-05-30 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="News",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created", models.DateTimeField(auto_now_add=True, verbose_name="Created")),
                ("updated", models.DateTimeField(auto_now=True, verbose_name="Updated")),
                ("deleted", models.BooleanField(default=False, verbose_name="Deleted")),
                ("title", models.CharField(max_length=256, verbose_name="Title")),
                ("preambule", models.CharField(max_length=1024, verbose_name="Preambule")),
                ("body", models.TextField(blank=True, null=True, verbose_name="Body")),
                ("body_as_markdown", models.BooleanField(default=False, verbose_name="As markdown")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]