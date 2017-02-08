from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import datetime

class teamProfile(models.Model):
    team=models.IntegerField()
    def __str__(self):
        return str(self.team)
# Create your models here.

class shirtImage(models.Model):
    addedBy=models.ForeignKey("UserProfile")
    team=models.ForeignKey(teamProfile)
    shirtImg=models.CharField(max_length=1000,blank=True,null=True)
    YEAR_CHOICES = []
    for r in range(2014, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    year = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    
    def __str__(self):
        return str(self.team)+" " + str(self.year)
        
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    team = models.ForeignKey(teamProfile,blank=True,null=True)
    shirtCount=models.IntegerField(blank=True,null=True)
    shirtImg=models.ForeignKey(shirtImage,blank=True,null=True)
    wanted=models.CommaSeparatedIntegerField(max_length=200,blank=True,null=True)
    post=models.BooleanField(default=True)
    
    
class message(models.Model):
    sentBy=models.ForeignKey(User,related_name="messageFrom")
    sentTo=models.ForeignKey(User,related_name="messageTo")
    content=models.CharField(max_length=10000)
    order=models.IntegerField()
    
