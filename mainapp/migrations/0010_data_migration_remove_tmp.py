from django.db import migrations


def forwards_func(apps, schema_editor):
    news_temp = apps.get_model("mainapp", "NewsTemp")
    news_temp.objects.all().delete()
    schema_editor.delete_model(news_temp)


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0009_data_migration_restore"),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
