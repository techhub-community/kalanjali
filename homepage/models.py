from django.db import models
from django import forms

# Create your models here.
class RegistrationModel(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=50)
    college = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    semester = models.IntegerField()
    event = models.CharField(max_length=20)
    txn_id = models.CharField(max_length=30,primary_key=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + " " + self.last_name
