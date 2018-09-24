from django.db import models
from django import forms
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class RegistrationModel(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=50)
    college = models.CharField(max_length=50)
    year = models.IntegerField()
    event = models.CharField(max_length=20)
    txn_id = models.CharField(max_length=30,primary_key=True)
    verified = models.BooleanField(default=False)


    def __str__(self):
        return self.name
