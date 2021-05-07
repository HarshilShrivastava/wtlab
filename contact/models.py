from django.db import models

# Create your models here.
class Contactus(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=255)
    Phone_no=models.CharField(max_length=13)
    message=models.TextField()