# Generated by Django 5.1.4 on 2025-01-03 00:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Wine",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=32)),
            ],
            options={
                "db_table": "wine",
            },
        ),
        migrations.CreateModel(
            name="WineDescription",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("description", models.TextField()),
                (
                    "wine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="descriptions",
                        to="wine.wine",
                    ),
                ),
            ],
            options={
                "db_table": "wine_description",
            },
        ),
        migrations.CreateModel(
            name="WineImage",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("image", models.CharField(max_length=100, null=True)),
                (
                    "wine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="wine.wine",
                    ),
                ),
            ],
            options={
                "db_table": "wine_image",
            },
        ),
        migrations.CreateModel(
            name="WinePrice",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("price", models.IntegerField()),
                (
                    "wine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="prices",
                        to="wine.wine",
                    ),
                ),
            ],
            options={
                "db_table": "wine_price",
            },
        ),
    ]
