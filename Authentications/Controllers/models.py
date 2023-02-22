from django.db import models

# Create your models here.
class Controllers(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30,unique=True)
    message=models.CharField(max_length=500,blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
