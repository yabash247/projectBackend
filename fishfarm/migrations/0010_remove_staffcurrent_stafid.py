# Generated by Django 5.1.1 on 2024-10-22 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("fishfarm", "0009_remove_staffcurrent_staffid"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="staffcurrent",
            name="stafId",
        ),
    ]
