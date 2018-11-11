from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()


class UserBase(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
# Create your models here.
