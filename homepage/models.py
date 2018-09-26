from django.db import models
from django import forms

# Create your models here.
class RegistrationModel(models.Model):
    number = models.IntegerField(default=0)
    coord_id = models.CharField(default="Nil",max_length=30)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=50)
    college = models.CharField(max_length=50)
    year = models.IntegerField()
    event = models.CharField(max_length=30)
    txn_id = models.CharField(max_length=50,primary_key=True)
    amount = models.IntegerField(default=0)
    verified = models.BooleanField(default=False)


    def __str__(self):
        return self.name
