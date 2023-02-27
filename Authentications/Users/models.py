from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
 
# Create your models here.
class Users(AbstractUser):
    is_active = models.BooleanField(default=True)
    is_client = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
    @receiver(post_save,sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender,instance=None,created=False,**kwargs):
        if created:
            Token.objects.create(user=instance)


'''user class to have the role on class'''
class  MASUsers(models.Model):
    user=models.OneToOneField(Users,related_name='maker',on_delete=models.CASCADE) 
    userName=models.CharField(max_length=20,unique=True)
    branch =models.CharField(max_length=40)
    role=models.CharField(max_length=30)
    phone=models.CharField(max_length=20)
    email=models.EmailField(max_length=40)
    createdAt= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userName

class Clients(models.Model):
    user=models.OneToOneField(Users,related_name='client',on_delete=models.CASCADE)
    branch=models.CharField(max_length=20)
    description=models.TextField()

    def __str__(self):
        return self.branch


