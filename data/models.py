from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    team = models.IntegerField(blank=True,null=True)
    shirtCount=models.IntegerField(blank=True,null=True)
    shirtImg=models.CharField(max_length=1000,blank=True,null=True)
    wanted=models.CommaSeparatedIntegerField(max_length=200,blank=True,null=True)
    post=models.BooleanField(default=False)
class teamProfile(models.Model):
    team=models.IntegerField()
    users=models.ForeignKey(User)
    shirtImg=models.CharField(max_length=1000,blank=True,null=True)
class message(models.Model):
    sentBy=models.ForeignKey(User,related_name="messageFrom")
    sentTo=models.ForeignKey(User,related_name="messageTo")
    content=models.CharField(max_length=10000)
    order=models.IntegerField()
    
