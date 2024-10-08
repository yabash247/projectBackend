from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from datetime import datetime 

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    paidMember = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def profile(self):
        profile = Profile.objects.get(user=self)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    bio = models.CharField(max_length=1000, null=True)
    image_ProfileLarge = models.ImageField(upload_to="images", null=True)
    image_ProfileSmall = models.ImageField(upload_to="images", null=True)
    image = models.ImageField(upload_to="images", null=True)
    instagram = models.CharField(max_length=100, null=True)
    twiter = models.CharField(max_length=100, null=True)
    tiktok = models.CharField(max_length=100, null=True)
    otherOnline = models.CharField(max_length=100, null=True)
    fb = models.CharField(max_length=100, null=True)
    website = models.CharField(max_length=100, null=True)
    phone = models.BigIntegerField(null=True)
    birthday = models.DateField(null=True)
    verified = models.BooleanField(default=False)

class Contacts(models.Model):
    userId = models.IntegerField(null=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    dateOfBirth = models.DateTimeField(null=True)
    dataCreated = models.DateTimeField(default=datetime.now)
    creatorId =  models.IntegerField(default=0)
    comments = models.CharField(max_length=1000, null=True)
    statuses = {
        "A": "Active",
        "UV": "Unverified",
        "S": "Suspended",
        "RE": "Removed"
    }
    status = models.CharField(max_length=2, choices=statuses)

class NextOfKin(models.Model):
    userContactId = models.IntegerField()
    kinContactId = models.IntegerField()
    Relationship = models.CharField(max_length=100, null=True)
    comments = models.CharField(max_length=1000, null=True)

class PaymentInfo(models.Model):
    userContactId = models.IntegerField()
    types = {
        "Ze": "Zelle",
        "BT": "Bank Transfer"
    }
    type = models.CharField(max_length=2, choices=types)
    bankName = models.CharField(max_length=100, null=True)
    Name = models.CharField(max_length=100, null=True)
    accountNumber = models.BigIntegerField()

class UserAddress(models.Model):
    userContactId = models.IntegerField()
    address = models.CharField(max_length=1000, null=True)
    title = models.CharField(max_length=100)
    dataCreated = models.DateTimeField(default=datetime.now)
    comments = models.CharField(max_length=1000, null=True)

class UsersSocialMedia(models.Model):
    userContactId = models.IntegerField()
    Name = models.CharField(max_length=100, null=True)
    link = models.CharField(max_length=100, null=True)
    types = {
        "M": "Main",
        "S": "Secondary"
    }
    type = models.CharField(max_length=2, choices=types)
    dataCreated = models.DateTimeField(default=datetime.now)
    comments = models.CharField(max_length=1000, null=True)

class ContactImage(models.Model):
    userContactId = models.IntegerField()
    image = models.ImageField(upload_to="images", null=True)
    types = {
        "L": "Licence",
        "P": "Passport",
        "FF": "FaceFront",
        "FS": "FaceSide",
        "FB": "fullBody",
    }
    type = models.CharField(max_length=2, choices=types)

class PhoneNumbers(models.Model):
    userContactId = models.IntegerField()
    Number = models.CharField(max_length=100, null=True)
    NetworkProvider = models.CharField(max_length=100, null=True)
    types = {
        "M": "Main",
        "S": "Secondary"
    }
    type = models.CharField(max_length=2, choices=types)
    Country = models.CharField(max_length=100, null=True)
    dataCreated = models.DateTimeField(default=datetime.now)
    comments = models.CharField(max_length=1000, null=True)

class Emails(models.Model):
    userContactId = models.IntegerField()
    Email = models.EmailField(max_length=254, null=True)
    types = {
        "M": "Main",
        "S": "Secondary"
    }
    type = models.CharField(max_length=2, choices=types)
    dataCreated = models.DateTimeField(default=datetime.now)
    comments = models.CharField(max_length=1000, null=True)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)