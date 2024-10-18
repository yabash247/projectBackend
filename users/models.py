from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    paidMember = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

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



def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)