# Generated by Django 5.1.4 on 2025-01-03 00:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Whiskey",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=32)),
            ],
            options={
                "db_table": "whiskey",
            },
        ),
        migrations.CreateModel(
            name="WhiskeyDescription",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("description", models.TextField()),
                (
                    "whiskey",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="descriptions",
                        to="whiskey.whiskey",
                    ),
                ),
            ],
            options={
                "db_table": "whiskey_description",
            },
        ),
        migrations.CreateModel(
            name="WhiskeyImage",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("image", models.CharField(max_length=100, null=True)),
                (
                    "whiskey",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="whiskey.whiskey",
                    ),
                ),
            ],
            options={
                "db_table": "whiskey_image",
            },
        ),
        migrations.CreateModel(
            name="WhiskeyPrice",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("price", models.IntegerField()),
                (
                    "whiskey",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="prices",
                        to="whiskey.whiskey",
                    ),
                ),
            ],
            options={
                "db_table": "whiskey_price",
            },
        ),
    ]
