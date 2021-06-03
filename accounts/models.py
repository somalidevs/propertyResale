from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from django.utils.text import slugify



Gender = (('male','male'),('female','female'))
Role=(('buyer','buyer'),('seller','seller'))


class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True,null=True)
    fullname=models.CharField(max_length=100,blank=True,null=True)
    gender = models.CharField(max_length=10,choices=Gender,default='male')
    image = models.ImageField(upload_to='images',default='default.jpg')
    phonenumber=models.CharField(max_length=15,blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    role=models.CharField(max_length=10,choices=Role,default='buyer')
    blocked=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
        
    def save(self,*args,**kwargs):
        if self.fullname:
                slug_gen = str(slugify(self.fullname))
        else:
            slug_gen = str(slugify(self.user.username))
        self.slug = slug_gen
        return super().save(*args,**kwargs)

