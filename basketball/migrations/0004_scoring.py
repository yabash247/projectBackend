# Generated by Django 5.1.1 on 2024-11-03 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("basketball", "0003_staffcurrent"),
    ]

    operations = [
        migrations.CreateModel(
            name="Scoring",
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
                ("staffId", models.IntegerField()),
                ("clubId", models.IntegerField()),
                (
                    "scoringType",
                    models.CharField(
                        choices=[
                            ("FS", "FreeStyle"),
                            ("3P", "Three Points"),
                            ("CS", "Close Shots"),
                            ("MR", "Mid Range"),
                            ("LU", "Lay Up"),
                            ("FA", "Fade Away"),
                        ],
                        default="FS",
                        max_length=2,
                    ),
                ),
                (
                    "locationType",
                    models.CharField(
                        choices=[
                            ("NA", 0),
                            ("12", 12),
                            ("1", 1),
                            ("2", 2),
                            ("3", 3),
                            ("11", 11),
                            ("10", 10),
                            ("9", 9),
                        ],
                        default="FS",
                        max_length=2,
                    ),
                ),
            ],
        ),
    ]
