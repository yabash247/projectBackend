# Generated by Django 5.1.1 on 2024-10-24 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bsf", "0008_containerstat"),
    ]

    operations = [
        migrations.AlterField(
            model_name="containerstat",
            name="harveststage",
            field=models.CharField(
                choices=[
                    ("1", "First Insta"),
                    ("2", "Fourt Insta"),
                    ("5", "Fifth Insta"),
                    ("6", "PrePupa"),
                    ("7", "Pupa"),
                    ("0", "N/A"),
                ],
                max_length=2,
            ),
        ),
    ]