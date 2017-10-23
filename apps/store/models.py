from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import md5
import os, binascii
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX =re.compile('^[A-z]+$')

# Create your models here.
class UserManager(models.Manager):
    def register(self, postData):
        errors = []
        # Check whether email exists in db
        if User.objects.filter(email=postData['email']):
            errors.append('Email is already registered')
        # Validate first name
        if len(postData['first_name']) < 2:
            errors.append('First name must be at least 2 characters')
        elif not NAME_REGEX.match(postData['first_name']):
            errors.append('First name must only contain alphabet')
        # Validate last name
        if len(postData['last_name']) < 2:
            errors.append('Last name must be at least 2 characters')
        elif not NAME_REGEX.match(postData['last_name']):
            errors.append('Last name must only contain alphabet')
        # Validate email
        if len(postData['email']) < 1:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(postData['email']):
            errors.append('Invalid email format')
        # Validate password
        if len(postData['password']) < 8:
            errors.append('Password must be at least 8 characters')
        # Validate confirm password
        elif postData['password'] != postData['confirm']:
            errors.append('Passwords do not match')

        # if no errors
        if len(errors) == 0:
            # add salt and hash the password
            salt = binascii.b2a_hex(os.urandom(15))
            hashed_pw = md5.new(salt + postData['password']).hexdigest()
            # add to database
            User.objects.create(first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'], salt=salt, password=hashed_pw)

        return errors

    def login(self, postData):
        errors = []
        # if email is found in db
        if User.objects.filter(email=postData['email']):
            salt = User.objects.get(email=postData['email']).salt
            hashed_pw = md5.new(salt + postData['password']).hexdigest()
            # compare hashed passwords
            if User.objects.get(email=postData['email']).password != hashed_pw:
                errors.append('Incorrect password')
        # else if email is not found in db
        else:
            errors.append('Email has not been registered')
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    salt = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()

    def __str__(self):
        return str(self.id) + self.first_name + self.last_name + self.email + self.salt + self.password

class iphone(models.Model):
    name = models.CharField(max_length=45)
    color = models.CharField(max_length=45)
    price = models.CharField(max_length=45)
    