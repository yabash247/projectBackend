# Generated by Django 5.0.6 on 2024-09-17 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0023_stocking_pondid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocking',
            name='fromPondId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stocking',
            name='fromVendordId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stocking',
            name='toVendorId',
            field=models.IntegerField(null=True),
        ),
    ]
