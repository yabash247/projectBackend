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


#branch of a company. such as a farm
class Farm(models.Model):
    name = models.CharField(max_length=100)
    summary = models.CharField(max_length=1000, null=True)
    companyId = models.IntegerField()
    createdDate = models.DateField(default=datetime.now)
    creatorId = models.IntegerField()
    approverId = models.IntegerField()
    ownerTypes = {
        "User": "User",
        "Staff": "Staff",
        "Contacts": "Contacts"
    }
    ownerType = models.CharField(max_length=10, choices=ownerTypes) 
    contactId = models.IntegerField()
    addressId = models.IntegerField()
    stat = [
        ('A', 'Active'),
        ('PA', 'pendingApproval'),
        ('IA', 'InActive'),
    ]
    status = models.CharField( max_length=2, choices=stat, default='IA',)
    comments = models.CharField(max_length=1000, null=True)


class Staff(models.Model):
    userId = models.IntegerField(default=0)
    companyId = models.IntegerField()
    workPhone = models.CharField(max_length=100, unique=True) #option too select same as that in profile // avoid duplicates
    workEmail = models.EmailField(max_length=1000, null=True, unique=True) #option too select same as that in profile // avoid duplicates
    dataCreated = models.DateTimeField(default=datetime.now)
    joinedCompanyDate = models.DateTimeField(null=True) #only manager and higher with authority can add too this / only level 4 and above can edit wih permision from level 5
    comments = models.CharField(max_length=2000, null=True)
    addedById = models.IntegerField()
    approvedById = models.IntegerField()


class StaffCurrent(models.Model):
    staffId = models.IntegerField(default=0)
    creatorSaffId = models.IntegerField()
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


#class SecurityDog 



# **** Expenses ****

   # Dog Feed > dogProtient(fish stomach) > item 
        # Thunder,Max,Smart > beneficairy 
            #dogs
                #security 
                    #farm
            # > beneficary parrents 



