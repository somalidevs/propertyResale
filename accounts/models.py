from django.db import models

# Create your models here.
from django.contrib.auth.models import User




Gender = (('male','male'),('female','female'))
Role=(('buyer','buyer'),('seller','seller'))


class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)
    fullname=models.CharField(max_length=100,blank=True,null=True)
    gender = models.CharField(max_length=10,choices=Gender,default='male')
    image = models.ImageField(upload_to='images',default='default.png')
    phonenumber=models.CharField(max_length=15,blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    role=models.CharField(max_length=10,choices=Role,default='buyer')
    blocked=models.BooleanField(default=False)

    def __str__(self):
        return self.auth_token

