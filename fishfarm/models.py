from django.db import models
from datetime import datetime
from users.models import User

# Create your models here.

class Authority(models.Model):
    tableName = models.CharField(max_length=100)
    farmId = models.IntegerField(null=True)
    levels = [
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
        ('4', 'Four'),
        ('5', 'Five'),
    ]
    view = models.CharField( max_length=1, choices=levels, default=5,)
    add = models.CharField( max_length=1, choices=levels, default=5,)
    edit = models.CharField( max_length=1, choices=levels, default=5,)
    delete = models.CharField( max_length=1, choices=levels, default=5,)
    accept = models.CharField( max_length=1, choices=levels, default=5,)
    approve = models.CharField( max_length=1, choices=levels, default=5,)


class Staff(models.Model):
    userId = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    companyId = models.IntegerField()
    workPhone = models.CharField(max_length=100, unique=True) #option too select same as that in profile // avoid duplicates
    workEmail = models.EmailField(max_length=1000, null=True, unique=True) #option too select same as that in profile // avoid duplicates
    dataCreated = models.DateTimeField(default=datetime.now)
    joinedCompanyDate = models.DateTimeField(null=True) #only manager and higher with authority can add too this / only level 4 and above can edit wih permision from level 5
    comments = models.CharField(max_length=2000, null=True)

    USERNAME_FIELD = 'userId'

    #address = models.CharField(max_length=1000, null=True)
    #relationId = models.IntegerField(null=True)
    #individualPaymentMethodTd


class StaffCurrent(models.Model):
    staffId = models.IntegerField()
    creatorSaffId = models.ForeignKey(
        'Staff',
        on_delete=models.CASCADE,
    )
    approvalSaffId = models.IntegerField(null=True)
    position = models.CharField(max_length=100)
    levels = [
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
        ('4', 'Four'),
        ('5', 'Five'),
    ]
    level = models.CharField( max_length=10, choices=levels, default=1,)
    pay = models.DecimalField(max_digits=25, decimal_places=3)
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
    eventOccuredDate = models.DateTimeField(default=datetime.now)
    comments = models.CharField(max_length=1000, null=True)



class StaffOrgChart(models.Model):
    staffId = models.IntegerField(null=True)
    bossId = models.IntegerField(null=True)
    creatorSaffId = models.IntegerField(null=True)
    approvalSaffId = models.IntegerField(null=True)
    startDate = models.DateTimeField(default=datetime.now)
    endDate = models.DateTimeField(null=True)
    stat = [
        ('A', 'Active'),
        ('IA', 'InActive'),
    ]
    status = models.CharField( max_length=2, choices=stat, default='IA',)
