from django.db import models
from datetime import datetime

#branch of a company. such as a farm
class BasketballClub(models.Model):
    name = models.CharField(max_length=100)
    summary = models.CharField(max_length=1000, null=True)
    companyId = models.IntegerField()
    createdDate = models.DateField(default=datetime.now)
    creatorId = models.IntegerField()
    creatorTypes = {
        "User": "User",
        "Staff": "Staff",
        "Contacts": "Contacts"
    }
    creatorType = models.CharField(max_length=10, choices=creatorTypes)
    approverId = models.IntegerField()
    contactId = models.IntegerField()
    addressId = models.IntegerField()
    stat = [
        ('A', 'Active'),
        ('PA', 'pendingApproval'),
        ('IA', 'InActive'),
    ]
    status = models.CharField( max_length=2, choices=stat, default='IA')
    comments = models.CharField(max_length=1000, null=True)


class StaffCurrent(models.Model):
    staffId = models.IntegerField()
    creatorSaffId = models.IntegerField()
    approvalSaffId = models.IntegerField(null=True)
    position = models.CharField(max_length=100)
    levels = [
        ('One', 1),
        ('Two', 2),
        ('Three', 3),
        ('Four', 4),
        ('Five', 5),
    ]
    level = models.CharField( max_length=10, choices=levels, default=1)
    clubId = models.IntegerField()
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


class Scoring(models.Model):
    staffId = models.IntegerField()
    clubId = models.IntegerField()
    scoringTypes = [
        ('FS', 'FreeStyle'),
        ('3P', 'Three Points'),
        ('CS', 'Close Shots'),
        ('MR', 'Mid Range'),
        ('LU', 'Lay Up'),
        ('FA', 'Fade Away'),
        ('btll', 'L-B/W leg Score'),
        ('btl', 'R-B/W leg Score'),
        ('sgb', 'score and go back'),
         ('1v1', '1v1'),
    ]
    scoringType = models.CharField( max_length=5, choices=scoringTypes, default='FS',)
    #starting at the middle of the court
    locationTypes = [
        ('NA', 0),
        ('12', 12),
        ('1',  1),
        ('2', 2),
        ('3', 3),
        ('11', 11),
        ('10', 10),
        ('9', 9),
    ]
    locationType = models.CharField( max_length=2, choices=locationTypes, default='FS',)
    creatorSaffId = models.IntegerField(null=True)
    attempts = models.IntegerField(null=True)
    made = models.IntegerField(null=True)
    #Accuracy in %
    accuracy = models.DecimalField(max_digits=25, decimal_places=3, null=True)
    date = models.DateField(default=datetime.now)
    stat = [
        ('A', 'Approved'),
        ('PA', 'pendingApproval'),
        ('D', 'Declined'),
    ]
    status = models.CharField( max_length=2, choices=stat, default='PA')
















# Create your models here.
