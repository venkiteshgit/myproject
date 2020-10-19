from django.db import models

# Create your models here.
class Insured(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=200)
    ssn = models.IntegerField(default=99999999)
    phone_number = models.IntegerField(default=99999999)
    address1 = models.CharField(max_length=1024)
    address2 = models.CharField(max_length=1024)
    city = models.CharField(max_length=1024)
    country = models.CharField(max_length=3)
    zip_code = models.IntegerField(default=999999)
    dob = models.DateField()

