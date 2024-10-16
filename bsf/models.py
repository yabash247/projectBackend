from django.db import models
from datetime import datetime

# Create your models here.


class Batch(models.Model):
    farmId = models.IntegerField()

class Laying(models.Model):
    batchId = models.IntegerField()
    netId = models.IntegerField()
    layingStart = models.DateTimeField()
    layingStartVideo = models.ImageField(upload_to="images", null=True)
    layingMidVideo = models.ImageField(upload_to="images", null=True)
    layingEnd = models.DateTimeField()
    layingEndVideo = models.ImageField(upload_to="images", null=True)
    harvest = models.DecimalField(max_digits=25, decimal_places=10)
    harvestStat = [
        ('IP', 'InProgress'),
        ('C', 'Completed'),
        ('D', 'Delayed')
    ]
    harveststatus = models.CharField( max_length=2, choices=harvestStat)
    endResults= [
        ('S', 'Satisfacory'),
        ('G', 'Good'),
        ('O', 'Ok'),
        ('p', 'Poor'),
        ('B', 'Bad')
    ]
    endResult = models.CharField( max_length=2, choices=endResults)
    comment = models.CharField(max_length=1000, null=True)
    leadId = models.IntegerField()
    approverId = models.IntegerField()

class Net(models.Model):
    farmId = models.IntegerField()
    netNumber = models.IntegerField()

class Incubation(models.Model):
    batchId = models.IntegerField()
    incubatorId = models.IntegerField()
    incubateStart = models.DateTimeField()
    incubateStartVideo = models.ImageField(upload_to="images", null=True)
    incubateMidVideo = models.ImageField(upload_to="images", null=True)
    incubateEnd = models.DateTimeField()
    incubateEndVideo = models.ImageField(upload_to="images", null=True)
    harvest = models.DecimalField(max_digits=25, decimal_places=10)
    harvestStat = [
        ('IP', 'InProgress'),
        ('C', 'Completed'),
        ('D', 'Delayed')
    ]
    harveststatus = models.CharField( max_length=2, choices=harvestStat)
    endResults= [
        ('S', 'Satisfacory'),
        ('G', 'Good'),
        ('O', 'Ok'),
        ('p', 'Poor'),
        ('B', 'Bad')
    ]
    endResult = models.CharField( max_length=2, choices=endResults)
    comment = models.CharField(max_length=1000, null=True)
    leadId = models.IntegerField()
    approverId = models.IntegerField()

class Incubator(models.Model):
    farmId = models.IntegerField()
    incubatorNumber = models.IntegerField()


class Nursery(models.Model): 
    batchId = models.IntegerField()
    nurseryId = models.IntegerField()
    nurseryStart = models.DateTimeField()
    nurseryStartVideo = models.ImageField(upload_to="images", null=True)
    nurseryMidVideo = models.ImageField(upload_to="images", null=True)
    nurseryEnd = models.DateTimeField()
    nurseryEndVideo = models.ImageField(upload_to="images", null=True)
    harvest = models.DecimalField(max_digits=25, decimal_places=10)
    harvestStat = [
        ('IP', 'InProgress'),
        ('C', 'Completed'),
        ('D', 'Delayed')
    ]
    harveststatus = models.CharField( max_length=2, choices=harvestStat)
    endResults= [
        ('S', 'Satisfacory'),
        ('G', 'Good'),
        ('O', 'Ok'),
        ('p', 'Poor'),
        ('B', 'Bad')
    ]
    endResult = models.CharField( max_length=2, choices=endResults)
    comment = models.CharField(max_length=1000, null=True)
    leadId = models.IntegerField()
    approverId = models.IntegerField()

class NurseryPond(models.Model):
    farmId = models.IntegerField()
    nurseryNumber = models.IntegerField()


class GrowOut(models.Model): 
    batchId = models.IntegerField()
    growOutId = models.IntegerField()
    growOutStart = models.DateTimeField()
    growOutStartVideo = models.ImageField(upload_to="images", null=True)
    growOutMidVideo = models.ImageField(upload_to="images", null=True)
    growOutEnd = models.DateTimeField()
    growOutEndVideo = models.ImageField(upload_to="images", null=True)
    harvest = models.DecimalField(max_digits=25, decimal_places=10)
    harvestStat = [
        ('IP', 'InProgress'),
        ('C', 'Completed'),
        ('D', 'Delayed')
    ]
    harveststatus = models.CharField( max_length=2, choices=harvestStat)
    endResults= [
        ('S', 'Satisfacory'),
        ('G', 'Good'),
        ('O', 'Ok'),
        ('p', 'Poor'),
        ('B', 'Bad')
    ]
    endResult = models.CharField( max_length=2, choices=endResults)
    comment = models.CharField(max_length=1000, null=True)
    leadId = models.IntegerField()
    approverId = models.IntegerField()

class GrowOutPond(models.Model):
    farmId = models.IntegerField()
    growOutNumber = models.IntegerField()


class Maturity(models.Model): 
    batchId = models.IntegerField()
    maturityId = models.IntegerField()
    maturityStart = models.DateTimeField()
    maturityStartVideo = models.ImageField(upload_to="images", null=True)
    maturityMidVideo = models.ImageField(upload_to="images", null=True)
    maturityEnd = models.DateTimeField()
    maturityEndVideo = models.ImageField(upload_to="images", null=True)
    harvest = models.DecimalField(max_digits=25, decimal_places=10)
    harvestStat = [
        ('IP', 'InProgress'),
        ('C', 'Completed'),
        ('D', 'Delayed')
    ]
    harveststatus = models.CharField( max_length=2, choices=harvestStat)
    endResults= [
        ('S', 'Satisfacory'),
        ('G', 'Good'),
        ('O', 'Ok'),
        ('p', 'Poor'),
        ('B', 'Bad')
    ]
    endResult = models.CharField( max_length=2, choices=endResults)
    comment = models.CharField(max_length=1000, null=True)
    leadId = models.IntegerField()
    approverId = models.IntegerField()

class MaturityPond(models.Model):
    farmId = models.IntegerField()
    maturityNumber = models.IntegerField()