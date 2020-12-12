from django.db import models
# Create your models here.

class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    source_id = models.IntegerField()
    source_name= models.CharField(max_length=32)
    name= models.CharField(max_length=32)
    website= models.CharField(max_length=256)
    email= models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    address = models.CharField(max_length=32)
    postal_code = models.CharField(max_length=256)
    city = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    
    def __str__(self):
        return self.name


class Match(models.Model):
    id = models.IntegerField(primary_key=True)
    left_company_id = models.IntegerField()
    right_company_id = models.IntegerField()
    
    
   