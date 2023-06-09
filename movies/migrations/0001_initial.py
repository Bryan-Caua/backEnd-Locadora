# Generated by Django 4.1.7 on 2023-02-16 14:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
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
                ("title", models.CharField(max_length=127)),
                (
                    "duration",
                    models.IntegerField(default=None, max_length=10, null=True),
                ),
                (
                    "rating",
                    models.CharField(
                        choices=[
                            ("G", "G"),
                            ("PG", "Pg"),
                            ("PG-13", "Pg13"),
                            ("R", "R"),
                            ("NC-17", "Nc17"),
                        ],
                        default="G",
                        max_length=20,
                    ),
                ),
                ("synopsis", models.CharField(default=None, max_length=200, null=True)),
            ],
        ),
    ]
