from django.db import models
from datetime import datetime

# Create your models here.

class Authority(models.Model):
    tableName = models.CharField(max_length=100)
    farmId = models.IntegerField(null=True)
    levels = [
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
    ]
    add = models.CharField( max_length=1, choices=levels, default=5,)
    edit = models.CharField( max_length=1, choices=levels, default=5,)
    delete = models.CharField( max_length=1, choices=levels, default=5,)
    accept = models.CharField( max_length=1, choices=levels, default=5,)
    approve = models.CharField( max_length=1, choices=levels, default=5,)


class Staff(models.Model):
    userId = models.IntegerField(unique=True)
    companyId = models.IntegerField()
    workPhone = models.CharField(max_length=100)
    workEmail = models.EmailField(max_length=1000, null=True)
    dataCreated = models.DateTimeField(default=datetime.now)
    joinedCompanyDate = models.DateTimeField(null=True)
    comments = models.CharField(max_length=2000, null=True)

    #address = models.CharField(max_length=1000, null=True)
    #relationId = models.IntegerField(null=True)
    #individualPaymentMethodTd


class StaffCurrent(models.Model):
    userId = models.IntegerField()
    position = models.CharField(max_length=100)
    levels = [
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
    ]
    level = models.CharField( max_length=10, choices=levels, default=1,)
    pay = models.DecimalField(max_digits=25, decimal_places=10)
    farmId = models.IntegerField()
    stat = [
        ('A', 'Active'),
        ('F', 'Fired'),
        ('R', 'Resigned'),
        ('RT', 'Retired'),
        ('OS', 'OfferSent'),
        ('PA', 'pendingApproval'),
        ('IA', 'InActive'),
    ]
    status = models.CharField( max_length=2, choices=stat, default='IA',)
    dataCreated = models.DateTimeField(default=datetime.now)
    comments = models.CharField(max_length=1000, null=True)



class StaffOrgChart(models.Model):
    staffId = models.IntegerField(null=True)
    bossId = models.IntegerField(null=True)
    startDate = models.DateTimeField(default=datetime.now)
    endDate = models.DateTimeField(null=True)
    stat = [
        ('A', 'Active'),
        ('IA', 'InActive'),
    ]
    status = models.CharField( max_length=2, choices=stat, default='IA',)
