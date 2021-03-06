# Generated by Django 3.2.13 on 2022-05-30 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0003_lessons_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="Teachers",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created", models.DateTimeField(auto_now_add=True, verbose_name="Created")),
                ("updated", models.DateTimeField(auto_now=True, verbose_name="Updated")),
                ("deleted", models.BooleanField(default=False, verbose_name="Deleted")),
                ("name_first", models.CharField(max_length=128, verbose_name="Name")),
                ("name_second", models.CharField(max_length=128, verbose_name="Surname")),
                ("day_birth", models.DateField(default=False)),
                ("course", models.ManyToManyField(to="mainapp.Courses")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
