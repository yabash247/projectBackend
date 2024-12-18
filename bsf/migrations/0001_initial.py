# Generated by Django 5.0.6 on 2024-10-18 23:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GrowOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batchId', models.IntegerField()),
                ('growOutId', models.IntegerField()),
                ('growOutStart', models.DateTimeField()),
                ('growOutStartVideo', models.ImageField(null=True, upload_to='images')),
                ('growOutMidVideo', models.ImageField(null=True, upload_to='images')),
                ('growOutEnd', models.DateTimeField()),
                ('growOutEndVideo', models.ImageField(null=True, upload_to='images')),
                ('harvest', models.DecimalField(decimal_places=10, max_digits=25)),
                ('harveststatus', models.CharField(choices=[('IP', 'InProgress'), ('C', 'Completed'), ('D', 'Delayed')], max_length=2)),
                ('endResult', models.CharField(choices=[('S', 'Satisfacory'), ('G', 'Good'), ('O', 'Ok'), ('p', 'Poor'), ('B', 'Bad')], max_length=2)),
                ('comment', models.CharField(max_length=1000, null=True)),
                ('leadId', models.IntegerField()),
                ('approverId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GrowOutPond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmId', models.IntegerField()),
                ('growOutNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Incubation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batchId', models.IntegerField()),
                ('incubatorId', models.IntegerField()),
                ('incubateStart', models.DateTimeField()),
                ('incubateStartVideo', models.ImageField(null=True, upload_to='images')),
                ('incubateMidVideo', models.ImageField(null=True, upload_to='images')),
                ('incubateEnd', models.DateTimeField()),
                ('incubateEndVideo', models.ImageField(null=True, upload_to='images')),
                ('harvest', models.DecimalField(decimal_places=10, max_digits=25)),
                ('harveststatus', models.CharField(choices=[('IP', 'InProgress'), ('C', 'Completed'), ('D', 'Delayed')], max_length=2)),
                ('endResult', models.CharField(choices=[('S', 'Satisfacory'), ('G', 'Good'), ('O', 'Ok'), ('p', 'Poor'), ('B', 'Bad')], max_length=2)),
                ('comment', models.CharField(max_length=1000, null=True)),
                ('leadId', models.IntegerField()),
                ('approverId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Incubator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmId', models.IntegerField()),
                ('incubatorNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Maturity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batchId', models.IntegerField()),
                ('maturityId', models.IntegerField()),
                ('maturityStart', models.DateTimeField()),
                ('maturityStartVideo', models.ImageField(null=True, upload_to='images')),
                ('maturityMidVideo', models.ImageField(null=True, upload_to='images')),
                ('maturityEnd', models.DateTimeField()),
                ('maturityEndVideo', models.ImageField(null=True, upload_to='images')),
                ('harvest', models.DecimalField(decimal_places=10, max_digits=25)),
                ('harveststatus', models.CharField(choices=[('IP', 'InProgress'), ('C', 'Completed'), ('D', 'Delayed')], max_length=2)),
                ('endResult', models.CharField(choices=[('S', 'Satisfacory'), ('G', 'Good'), ('O', 'Ok'), ('p', 'Poor'), ('B', 'Bad')], max_length=2)),
                ('comment', models.CharField(max_length=1000, null=True)),
                ('leadId', models.IntegerField()),
                ('approverId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MaturityPond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmId', models.IntegerField()),
                ('maturityNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Net',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmId', models.IntegerField()),
                ('netNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nursery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batchId', models.IntegerField()),
                ('nurseryId', models.IntegerField()),
                ('nurseryStart', models.DateTimeField()),
                ('nurseryStartVideo', models.ImageField(null=True, upload_to='images')),
                ('nurseryMidVideo', models.ImageField(null=True, upload_to='images')),
                ('nurseryEnd', models.DateTimeField()),
                ('nurseryEndVideo', models.ImageField(null=True, upload_to='images')),
                ('harvest', models.DecimalField(decimal_places=10, max_digits=25)),
                ('harveststatus', models.CharField(choices=[('IP', 'InProgress'), ('C', 'Completed'), ('D', 'Delayed')], max_length=2)),
                ('endResult', models.CharField(choices=[('S', 'Satisfacory'), ('G', 'Good'), ('O', 'Ok'), ('p', 'Poor'), ('B', 'Bad')], max_length=2)),
                ('comment', models.CharField(max_length=1000, null=True)),
                ('leadId', models.IntegerField()),
                ('approverId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NurseryPond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmId', models.IntegerField()),
                ('nurseryNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Laying',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('netId', models.IntegerField()),
                ('layingStart', models.DateTimeField()),
                ('layingStartVideo', models.ImageField(null=True, upload_to='images')),
                ('layingMidVideo', models.ImageField(null=True, upload_to='images')),
                ('layingEnd', models.DateTimeField()),
                ('layingEndVideo', models.ImageField(null=True, upload_to='images')),
                ('harvest', models.DecimalField(decimal_places=10, max_digits=25)),
                ('harveststatus', models.CharField(choices=[('IP', 'InProgress'), ('C', 'Completed'), ('D', 'Delayed')], max_length=2)),
                ('endResult', models.CharField(choices=[('S', 'Satisfacory'), ('G', 'Good'), ('O', 'Ok'), ('p', 'Poor'), ('B', 'Bad')], max_length=2)),
                ('comment', models.CharField(max_length=1000, null=True)),
                ('leadId', models.IntegerField()),
                ('approverId', models.IntegerField()),
                ('batchId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsf.batch')),
            ],
        ),
    ]
