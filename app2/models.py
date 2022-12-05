from django.db import models

# Create your models here.

class employee(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    salary = models.IntegerField()
    status = models.BooleanField()
    class Meta:
        db_table ='app2_employee'

class partners(models.Model):
    name = models.CharField(max_length=100)
    buisnessname = models.CharField(max_length=100)
    contactperson1 = models.CharField(max_length=100)

    contactemail1 = models.CharField(max_length=100)
    contactperson2 = models.CharField(max_length=100)
    contactdetails2 = models.CharField(max_length=100)
    contactemail2 = models.CharField(max_length=100)
    mailingaddress = models.CharField(max_length=100)
    zipcode1 = models.CharField(max_length=100)
    billingaddress = models.CharField(max_length=100)
    zipcode2 = models.CharField(max_length=100)
    contactdetails1 = models.CharField(max_length=100)

class Meta:
     db_table = 'partners'

class merchants(models.Model):
    id1 = models.IntegerField()
    placeorderid = models.IntegerField()
    offerid = models.IntegerField()
    typeofpackage = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    itemprice = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    merchantname = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    billingtype = models.CharField(max_length=100)

class Meta:
     db_table = 'merchants'

class manufacturer(models.Model):
    id1 = models.IntegerField()
    name = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    passcode = models.CharField(max_length=100)
    billingtype = models.CharField(max_length=100)
    materialtype = models.CharField(max_length=100)
    addonstype = models.CharField(max_length=100)
    addonsnumber = models.CharField(max_length=100)

class Meta:
     db_table = 'manufacturer'


class openticket(models.Model):
         name = models.CharField(max_length=100)
         email = models.CharField(max_length=100)

class Meta:
     db_table = 'openticket'