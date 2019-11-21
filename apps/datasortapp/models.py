from __future__ import unicode_literals
from django.db import models
import re
from datetime import datetime
import time

class userManager(models.Manager):
    def basic_validator(self,postData):
        errors={}
        usercur=Users.objects.filter(email=postData['email'])
        if usercur:
            errors['reg']='Email in use'
        if len(postData['fname'])<2:
            errors['name']='First Name needs to be more than 2 characters'
        if len(postData['lname'])<2:
            errors['alias']='Last Name needs to be more than 2 characters'
        if len(postData['pw'])<8:
            errors['pw']='Password must be longer than 8 characters'
        if postData['cpw'] != postData['pw']:
            errors['pwconf']= 'passwords do not match'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):      
            errors['email'] = ("Invalid email address!")
        password = postData['pw']
        if not re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{6,12}$", password):
            errors['pwtype']='needs uppercase, lowercaste, special characets'
        
        return errors
    def login_validator(self,postData):
        errors={}
        if not Users.objects.filter(email=postData['email']):
            errors['login']='User has not registered'
        return errors

class dataManager(models.Manager):
    pass

class Users(models.Model):
    first=models.CharField(max_length=255)
    last=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = userManager()

class DataSearch(models.Model):
    dataInput=models.TextField()
    userlink=models.ForeignKey(Users, related_name='dataQuery')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=dataManager()


