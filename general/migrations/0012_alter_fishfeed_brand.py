# Generated by Django 5.1.1 on 2024-10-23 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("general", "0011_alter_fishfeed_size"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fishfeed",
            name="brand",
            field=models.CharField(
                choices=[("Kg", "Blue Crown"), ("Ibs", "Cupen")], max_length=5
            ),
        ),
    ]
