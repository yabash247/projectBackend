# Generated by Django 5.1.1 on 2024-10-22 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fishfarm", "0003_remove_staffcurrent_creatorsaffid"),
    ]

    operations = [
        migrations.AddField(
            model_name="staffcurrent",
            name="creatorSaffId",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
