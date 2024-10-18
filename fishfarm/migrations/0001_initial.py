# Generated by Django 5.1.1 on 2024-10-18 04:16

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Authority",
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
                ("tableName", models.CharField(max_length=100)),
                ("farmId", models.IntegerField(null=True)),
                (
                    "view",
                    models.CharField(
                        choices=[
                            ("1", "One"),
                            ("2", "Two"),
                            ("3", "Three"),
                            ("4", "Four"),
                            ("5", "Five"),
                        ],
                        default=5,
                        max_length=1,
                    ),
                ),
                (
                    "add",
                    models.CharField(
                        choices=[
                            ("1", "One"),
                            ("2", "Two"),
                            ("3", "Three"),
                            ("4", "Four"),
                            ("5", "Five"),
                        ],
                        default=5,
                        max_length=1,
                    ),
                ),
                (
                    "edit",
                    models.CharField(
                        choices=[
                            ("1", "One"),
                            ("2", "Two"),
                            ("3", "Three"),
                            ("4", "Four"),
                            ("5", "Five"),
                        ],
                        default=5,
                        max_length=1,
                    ),
                ),
                (
                    "delete",
                    models.CharField(
                        choices=[
                            ("1", "One"),
                            ("2", "Two"),
                            ("3", "Three"),
                            ("4", "Four"),
                            ("5", "Five"),
                        ],
                        default=5,
                        max_length=1,
                    ),
                ),
                (
                    "accept",
                    models.CharField(
                        choices=[
                            ("1", "One"),
                            ("2", "Two"),
                            ("3", "Three"),
                            ("4", "Four"),
                            ("5", "Five"),
                        ],
                        default=5,
                        max_length=1,
                    ),
                ),
                (
                    "approve",
                    models.CharField(
                        choices=[
                            ("1", "One"),
                            ("2", "Two"),
                            ("3", "Three"),
                            ("4", "Four"),
                            ("5", "Five"),
                        ],
                        default=5,
                        max_length=1,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Staff",
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
                ("userId", models.IntegerField(unique=True)),
                ("companyId", models.IntegerField()),
                ("workPhone", models.CharField(max_length=100, unique=True)),
                (
                    "workEmail",
                    models.EmailField(max_length=1000, null=True, unique=True),
                ),
                ("dataCreated", models.DateTimeField(default=datetime.datetime.now)),
                ("joinedCompanyDate", models.DateTimeField(null=True)),
                ("comments", models.CharField(max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="StaffOrgChart",
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
                ("staffId", models.IntegerField(null=True)),
                ("bossId", models.IntegerField(null=True)),
                ("creatorSaffId", models.IntegerField(null=True)),
                ("approvalSaffId", models.IntegerField(null=True)),
                ("startDate", models.DateTimeField(default=datetime.datetime.now)),
                ("endDate", models.DateTimeField(null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("A", "Active"), ("IA", "InActive")],
                        default="IA",
                        max_length=2,
                    ),
                ),
            ],
        ),
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
                ("approvalSaffId", models.IntegerField(null=True)),
                ("position", models.CharField(max_length=100)),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("1", "One"),
                            ("2", "Two"),
                            ("3", "Three"),
                            ("4", "Four"),
                            ("5", "Five"),
                        ],
                        default=1,
                        max_length=10,
                    ),
                ),
                ("pay", models.DecimalField(decimal_places=3, max_digits=25)),
                ("farmId", models.IntegerField()),
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
                (
                    "creatorSaffId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="fishfarm.staff"
                    ),
                ),
            ],
        ),
    ]
