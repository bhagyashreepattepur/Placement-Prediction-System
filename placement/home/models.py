from django.db import models

# Create your models here.
class signup(models.Model):
    username=models.CharField(max_length=90)
    password=models.CharField(max_length=90)
    DOB=models.DateField(max_length=8)
    gender=models.CharField(max_length=90)
    phone=models.IntegerField(max_length=90)
    place=models.CharField(max_length=90)

class signin(models.Model):
    username=models.CharField(max_length=90)
    password=models.CharField(max_length=90)