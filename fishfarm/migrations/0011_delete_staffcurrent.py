# Generated by Django 5.1.1 on 2024-10-22 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("fishfarm", "0010_remove_staffcurrent_stafid"),
    ]

    operations = [
        migrations.DeleteModel(
            name="StaffCurrent",
        ),
    ]
