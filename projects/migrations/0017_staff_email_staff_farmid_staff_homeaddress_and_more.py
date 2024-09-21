# Generated by Django 5.0.6 on 2024-09-16 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_staff_stocking_addedimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='email',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='farmId',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='homeAddress',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='phoneMain',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='phoneSecondary',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='relationId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
