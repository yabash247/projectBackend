# Generated by Django 5.1.1 on 2024-10-22 19:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("general", "0008_rename_branchid_authority_userid_and_more"),
    ]

    operations = [
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
                ("userId", models.IntegerField(default=0)),
                ("companyId", models.IntegerField()),
                ("workPhone", models.CharField(max_length=100, unique=True)),
                (
                    "workEmail",
                    models.EmailField(max_length=1000, null=True, unique=True),
                ),
                ("dataCreated", models.DateTimeField(default=datetime.datetime.now)),
                ("joinedCompanyDate", models.DateTimeField(null=True)),
                ("comments", models.CharField(max_length=2000, null=True)),
                ("addedById", models.IntegerField()),
                ("approvedById", models.IntegerField()),
            ],
        ),
    ]
