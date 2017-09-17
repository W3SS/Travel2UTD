from django.db import models

# Create your models here.
class Bus(models.Model):
    latitude = models.DecimalField(max_digits=12,decimal_places=10)
    longitude = models.DecimalField(max_digits=12,decimal_places=10)
    timestamp= models.BigIntegerField()
