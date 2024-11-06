# Generated by Django 5.1.1 on 2024-10-23 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("general", "0014_rename_weight_fishfeed_quantity_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fishfeed",
            name="size",
            field=models.DecimalField(
                choices=[
                    (0.5, "0.5mm"),
                    (0.8, "0.8mm"),
                    (1.5, "1.5mm"),
                    (2, "2mm"),
                    (3, "3mm"),
                    (4, "4mm"),
                    (6, "6mm"),
                    (9, "9mm"),
                ],
                decimal_places=2,
                max_digits=4,
            ),
        ),
    ]
