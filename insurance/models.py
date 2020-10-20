from django.db import models

# Create your models here.
class Insured(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=200)
    ssn = models.CharField(default=999-99-9999,max_length=15)
    phone_number = models.CharField(default=99-999999999,max_length=15)
    address1 = models.CharField(max_length=1024)
    address2 = models.CharField(max_length=1024)
    city = models.CharField(max_length=1024)
    country = models.CharField(max_length=3)
    zip_code = models.CharField(default=999999,max_length=30)
    dob = models.DateField()

