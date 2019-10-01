from django.db import models

# Create your models here.
class PromoSmsModel(models.Model):
    phone = models.CharField(max_length=11)
    sms_sent = models.BooleanField(default=False)
