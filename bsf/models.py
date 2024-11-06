from django.db import models
from datetime import datetime

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

class Batch(models.Model):
    farmId = models.IntegerField()

class Net(models.Model):
    farmId = models.IntegerField()
    netNumber = models.IntegerField()

class NetStat(models.Model):
    batchNumber = models.IntegerField()
    netNumber = models.IntegerField()
    stat= [
        ('E', 'Empty'),
        ('NR', 'Need Repair'),
        ('IU', 'In USE'),
        ('HC', 'Harvest Completed'),
        ('NC', 'Need Cleaning')
    ]
    status = models.CharField( max_length=2, choices=stat)
    eggiesSetDate = models.DateField()
    eggiesRemovedDate = models.DateField()
    eggiesHarvested = models.DecimalField(max_digits=5, decimal_places=2, default=0)#in grams

class Container(models.Model):
    farmId = models.IntegerField()
    containerName = models.CharField(max_length=100)
    containerTypes = {
        "CP": "Concrete Pond",
        "PC": "Plastic Container",
        "RT": "Rubber Tire",
    }
    containerType = models.CharField(max_length=5, choices=containerTypes)
    containerUses = {
        "I": "Incubator",
        "N": "Nursery",
        "GO": "Grow Out",
        "M": "Mutiple",
    }
    containerUse = models.CharField(max_length=5, choices=containerUses, default='M')

class ContainerStat(models.Model):
    batchNumber = models.IntegerField()
    containerNumber = models.IntegerField()
    stat= [
        ('E', 'Empty'),
        ('NR', 'Need Repair'),
        ('IU', 'In USE'),
        ('HC', 'Harvest Completed')
    ]
    status = models.CharField( max_length=2, choices=stat)
    harveststages= [
        ('1', 'First Insta'), #Eggies > Incubtion
        ('2', 'Second Insta'), #Incubation > Nursery
        ('5', 'Fifth Insta'), #Nursery > Growout
        ('6', 'PrePupa'),
        ('7', 'Pupa'),
        ('0', 'N/A'),
    ]
    harveststage = models.CharField( max_length=2, choices=harveststages, default='0')
    setDate = models.DateField(null=True)
    removedDate = models.DateField(null=True)
    harvestWeight = models.DecimalField(max_digits=5, decimal_places=2, default=0)#in grams
    leadId = models.IntegerField(null=True)
    approverId = models.IntegerField(null=True)


class StaffCurrent(models.Model):
    staffId = models.IntegerField()
    creatorSaffId = models.IntegerField(null=True)
    approvalSaffId = models.IntegerField(null=True)
    position = models.CharField(max_length=100)
    levels = [
        ('One', 1),
        ('Two', 2),
        ('Three', 3),
        ('Four', 4),
        ('Five', 5),
    ]
    level = models.CharField( max_length=5, choices=levels, default=1,)
    pay = models.DecimalField(max_digits=3, decimal_places=3)
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
    status = models.CharField( max_length=2, choices=stat, default='IA')
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
    status = models.CharField( max_length=2, choices=stat, default='IA')

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


