# Generated by Django 5.1.1 on 2024-11-02 06:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bsf", "0020_alter_staffcurrent_level"),
    ]

    operations = [
        migrations.CreateModel(
            name="Farm",
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
                ("name", models.CharField(max_length=100)),
                ("summary", models.CharField(max_length=1000, null=True)),
                ("companyId", models.IntegerField()),
                ("createdDate", models.DateField(default=datetime.datetime.now)),
                ("creatorId", models.IntegerField()),
                ("approverId", models.IntegerField()),
                (
                    "ownerType",
                    models.CharField(
                        choices=[
                            ("User", "User"),
                            ("Staff", "Staff"),
                            ("Contacts", "Contacts"),
                        ],
                        max_length=10,
                    ),
                ),
                ("contactId", models.IntegerField()),
                ("addressId", models.IntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("A", "Active"),
                            ("PA", "pendingApproval"),
                            ("IA", "InActive"),
                        ],
                        default="IA",
                        max_length=2,
                    ),
                ),
                ("comments", models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]