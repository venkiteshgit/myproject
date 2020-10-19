from django.db import models

# Create your models here.
class Insured(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12)
    address1 = models.CharField(max_length=1024)
    address2 = models.CharField(max_length=1024)
    city = models.CharField(max_length=1024)
    country = models.CharField(max_length=3)
    zip_code = models.CharField(max_length=12)
    dob = models.DateField()

