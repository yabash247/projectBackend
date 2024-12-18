# Generated by Django 5.0.6 on 2024-10-21 05:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivitiesImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activityId', models.IntegerField()),
                ('pondId', models.IntegerField()),
                ('projectId', models.IntegerField()),
                ('title', models.CharField(max_length=100, null=True)),
                ('src', models.ImageField(null=True, upload_to='images')),
                ('comments', models.CharField(max_length=1000, null=True)),
                ('uploadDate', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='activityNames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('creatorId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('creatorId', models.IntegerField()),
                ('contactName', models.CharField(max_length=100)),
                ('contactPhone', models.IntegerField()),
                ('contactEmail', models.EmailField(max_length=254)),
                ('instagram', models.CharField(max_length=100)),
                ('facebook', models.CharField(max_length=100)),
                ('status', models.IntegerField()),
                ('Address', models.CharField(max_length=1000)),
                ('City', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
                ('Country', models.CharField(max_length=100)),
                ('zipCode', models.IntegerField()),
                ('comments', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField(null=True)),
                ('firstName', models.CharField(max_length=100, null=True)),
                ('lastName', models.CharField(max_length=100, null=True)),
                ('dateOfBirth', models.DateTimeField(null=True)),
                ('dataCreated', models.DateTimeField(default=datetime.datetime.now)),
                ('creatorId', models.IntegerField(null=True)),
                ('phoneOne', models.IntegerField(null=True)),
                ('phoneTwo', models.IntegerField(null=True)),
                ('emailOne', models.EmailField(max_length=254, null=True)),
                ('emailTwo', models.EmailField(max_length=254, null=True)),
                ('instagram', models.CharField(max_length=100, null=True)),
                ('facebook', models.CharField(max_length=100, null=True)),
                ('status', models.IntegerField(null=True)),
                ('Address', models.CharField(max_length=1000, null=True)),
                ('comments', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactId', models.IntegerField(default=0)),
                ('farmId', models.IntegerField()),
                ('position', models.CharField(max_length=100)),
                ('employmentDate', models.DateTimeField(null=True)),
                ('positionDate', models.DateTimeField(null=True)),
                ('status', models.IntegerField(default=1)),
                ('comments', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmId', models.IntegerField()),
                ('itemDescription', models.CharField(max_length=2000)),
                ('unitCost', models.IntegerField(null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('totalcost', models.IntegerField()),
                ('expensesDate', models.DateTimeField()),
                ('paymentToId', models.IntegerField(null=True)),
                ('shopId', models.IntegerField(null=True)),
                ('comments', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='expenseItemTableLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expenseId', models.IntegerField()),
                ('itemId', models.IntegerField()),
                ('quantityPercentage', models.IntegerField()),
                ('costPercentage', models.IntegerField()),
                ('deliveryCostPercentage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ExpensesDisbursement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expenseId', models.IntegerField()),
                ('sharePecentage', models.IntegerField()),
                ('allocatedToId', models.IntegerField()),
                ('ItemsGroupId', models.IntegerField()),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='feeding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pondId', models.IntegerField()),
                ('feedDateTime', models.DateTimeField()),
                ('quantity', models.IntegerField()),
                ('reaction', models.CharField(choices=[('H', 'Hyper'), ('N', 'Normal'), ('BE', 'Barely Eating'), ('NE', 'Not Eating')], max_length=2)),
                ('brand', models.CharField(choices=[('IH', 'INHOUSE'), ('ECO', 'ECO'), ('BC', 'BLUE CROWN'), ('FLOAT', 'FLOAT'), ('CUPPEN', 'CUPPEN'), ('ALAQUA', 'ALAQUA'), ('BSF_LARVE', 'BSF_LARVE'), ('OTHERS', 'OTHERS')], default='active', max_length=10)),
                ('feedSize', models.CharField(choices=[('IH', 'INHOUSE'), ('ECO', 'ECO'), ('BC', 'BLUE CROWN'), ('FLOAT', 'FLOAT'), ('CUPPEN', 'CUPPEN'), ('ALAQUA', 'ALAQUA'), ('BSF_LARVE', 'BSF_LARVE'), ('OTHERS', 'OTHERS')], default='active', max_length=10)),
                ('comments', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='followupTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activityId', models.IntegerField()),
                ('notificationId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='followupTaskSuggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activityNamesId', models.IntegerField()),
                ('followupNameId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemParent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemId', models.IntegerField(null=True)),
                ('parentId', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=1000)),
                ('comments', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('projectId', models.IntegerField()),
                ('addedby_Id', models.IntegerField()),
                ('addedDate', models.DateField(default=datetime.datetime.now)),
                ('levels', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ponds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('projectId', models.IntegerField()),
                ('position_row', models.IntegerField()),
                ('position_col', models.IntegerField()),
                ('materialType', models.CharField(max_length=100)),
                ('depth', models.IntegerField()),
                ('lenght', models.IntegerField()),
                ('width', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PondstoDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pondId', models.IntegerField()),
                ('farmId', models.IntegerField()),
                ('pomdName', models.CharField(max_length=100, null=True)),
                ('taskName', models.CharField(max_length=100, null=True)),
                ('taskId', models.IntegerField()),
                ('createDate', models.DateTimeField(default=datetime.datetime.now)),
                ('dueDate', models.DateTimeField()),
                ('urgency', models.IntegerField()),
                ('status', models.IntegerField()),
                ('completeDate', models.DateTimeField(null=True)),
                ('requestorId', models.IntegerField()),
                ('assignedToId', models.IntegerField(null=True)),
                ('taskDetails', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=1000, null=True)),
                ('createdDate', models.DateField(default=datetime.datetime.now)),
                ('creatorId', models.IntegerField()),
                ('contactName', models.CharField(max_length=100, null=True)),
                ('contactPhone', models.BigIntegerField(null=True)),
                ('contactEmail', models.EmailField(max_length=254)),
                ('country', models.CharField(default='', max_length=100, null=True)),
                ('state', models.CharField(default='', max_length=100, null=True)),
                ('zipCode', models.IntegerField(default='')),
                ('fullsAddress', models.CharField(default='', max_length=1000, null=True)),
                ('area', models.IntegerField(default=0, null=True)),
                ('length', models.IntegerField(default=0, null=True)),
                ('width', models.IntegerField(default=0, null=True)),
                ('Status', models.IntegerField(default=1)),
                ('comments', models.CharField(max_length=1000, null=True)),
                ('website', models.CharField(max_length=200, null=True)),
                ('instagram', models.CharField(max_length=100, null=True)),
                ('facebook', models.CharField(max_length=100, null=True)),
                ('tiktok', models.CharField(max_length=100, null=True)),
                ('otherOnline', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='purchaseDelivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expenseId', models.IntegerField()),
                ('deliveryCost', models.IntegerField()),
                ('deliveryStatus', models.IntegerField()),
                ('shipperId', models.IntegerField(null=True)),
                ('mainHandler', models.CharField(max_length=1000)),
                ('secondaryHandler', models.CharField(max_length=1000, null=True)),
                ('shippingLocation', models.CharField(max_length=1000, null=True)),
                ('deliveryPickupLocation', models.CharField(max_length=1000)),
                ('estimatedShipTime', models.DateTimeField(max_length=1000)),
                ('estimatedDeliveryTime', models.DateTimeField()),
                ('receivierStaffId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pondId', models.IntegerField()),
                ('projectId', models.IntegerField()),
                ('dateSold', models.DateTimeField(default=datetime.datetime.now)),
                ('amount', models.IntegerField(null=True)),
                ('weight', models.IntegerField()),
                ('unitPrice', models.IntegerField()),
                ('fishId', models.IntegerField()),
                ('buyerId', models.IntegerField()),
                ('paid', models.IntegerField()),
                ('paymentBal', models.IntegerField()),
                ('status', models.IntegerField()),
                ('comments', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('managerId', models.IntegerField(null=True)),
                ('dateOfBirth', models.DateTimeField(null=True)),
                ('userId', models.IntegerField(null=True)),
                ('farmId', models.IntegerField()),
                ('phoneMain', models.CharField(max_length=100)),
                ('phoneSecondary', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=1000, null=True)),
                ('homeAddress', models.CharField(max_length=1000, null=True)),
                ('relationId', models.IntegerField(null=True)),
                ('dataCreated', models.DateTimeField(default=datetime.datetime.now)),
                ('employmentDate', models.DateTimeField(null=True)),
                ('status', models.IntegerField(default=1)),
                ('comments', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stocking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pondId', models.IntegerField()),
                ('toPondId', models.IntegerField()),
                ('toVendorId', models.IntegerField(null=True)),
                ('fromPondId', models.IntegerField(null=True)),
                ('fromVendordId', models.IntegerField(null=True)),
                ('waterLevel', models.IntegerField(null=True)),
                ('addedimage', models.ImageField(null=True, upload_to='images')),
                ('fishStage', models.CharField(max_length=1000, null=True)),
                ('type', models.CharField(max_length=100, null=True)),
                ('averageWeight', models.IntegerField(null=True)),
                ('totalWeight', models.IntegerField(null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('recordDate', models.DateTimeField(default=datetime.datetime.now)),
                ('fishId', models.IntegerField(null=True)),
                ('leadByName', models.CharField(max_length=100, null=True)),
                ('leadById', models.IntegerField(null=True)),
                ('assittedByName', models.CharField(max_length=100, null=True)),
                ('assittedById', models.IntegerField(null=True)),
                ('followupTask', models.CharField(max_length=100, null=True)),
                ('followupTaskDueDate', models.DateTimeField(null=True)),
                ('standing', models.CharField(max_length=1000, null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('addedQuantity', models.IntegerField(null=True)),
                ('addedSize', models.IntegerField(null=True)),
                ('addedWeight', models.IntegerField(null=True)),
                ('removed', models.IntegerField(null=True)),
                ('removedSize', models.IntegerField(null=True)),
                ('removedWeight', models.IntegerField(null=True)),
                ('comments', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='stockSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('unitCost', models.IntegerField(null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('totalcost', models.IntegerField()),
                ('totalWeight', models.IntegerField()),
                ('aveLength', models.IntegerField(null=True)),
                ('dob', models.DateTimeField()),
                ('purchaseDate', models.DateTimeField()),
                ('PurchaseId', models.IntegerField()),
                ('farmId', models.IntegerField()),
                ('vendorId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WaterChange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pondId', models.IntegerField()),
                ('eventDate', models.DateField()),
                ('depth', models.IntegerField()),
                ('preWaterColor', models.CharField(max_length=100)),
                ('preWaterCond', models.CharField(max_length=600)),
            ],
        ),
    ]
