# Generated by Django 5.1.1 on 2024-11-03 03:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("basketball", "0002_rename_ownertype_basketballclub_creatortype"),
    ]

    operations = [
        migrations.CreateModel(
            name="StaffCurrent",
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
                ("creatorSaffId", models.IntegerField()),
                ("approvalSaffId", models.IntegerField(null=True)),
                ("position", models.CharField(max_length=100)),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("One", 1),
                            ("Two", 2),
                            ("Three", 3),
                            ("Four", 4),
                            ("Five", 5),
                        ],
                        default=1,
                        max_length=10,
                    ),
                ),
                ("clubId", models.IntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("A", "Active"),
                            ("F", "Fired"),
                            ("R", "Resigned"),
                            ("RT", "Retired"),
                            ("OS", "OfferSent"),
                            ("PA", "pendingApproval"),
                            ("IA", "InActive"),
                        ],
                        default="IA",
                        max_length=2,
                    ),
                ),
                ("dataCreated", models.DateTimeField(default=datetime.datetime.now)),
                (
                    "eventOccuredDate",
                    models.DateTimeField(default=datetime.datetime.now),
                ),
                ("comments", models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
