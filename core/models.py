from django.db import models
from django_quill.fields import QuillField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.utils.text import slugify
from accounts.models import Customer




STATUS=(('active','active'),('inactive','inactive'))
class Property(models.Model):
        name=models.CharField(max_length=100)
        author=models.ForeignKey(Customer,on_delete=models.CASCADE)
        price=models.IntegerField()
        slug = models.SlugField(blank=True,null=True)
        catogory=models.ForeignKey('Category',on_delete=models.CASCADE)
        location=models.ForeignKey('Location',on_delete=models.CASCADE)
        images_1=models.ImageField(upload_to='images') 
        images_2=models.ImageField(upload_to='images') 
        images_3=models.ImageField(upload_to='images',blank=True,null=True) 
        description=QuillField(blank=True,null=True)
        status=models.CharField(max_length=10,choices=STATUS)
        p_type=models.CharField(max_length=100,blank=True,null=True)
        date_created=models.DateTimeField(auto_now=True)
        date_updated=models.DateTimeField(auto_now_add=True)

        def save(self,*args,**kwargs):
                if self.name:
                        slug_gen = str(slugify(self.name))
                self.slug = slug_gen


class Location(models.Model):
        name=models.CharField(max_length=100)



class Category(models.Model):
        name=models.CharField(max_length=100)


class Plan(models.Model):
        name = models.CharField(max_length=100)
        price = models.CharField(max_length=10)
        slug = models.SlugField(blank=True,null=True)
        # customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
        checked = models.BooleanField(default=False)
        auth_token = models.CharField(max_length=100)


        def save(self,*args,**kwargs):
                if self.name:
                        slug_gen = str(slugify(self.name))
                self.slug = slug_gen


class BankAccount(models.Model):
        name = models.CharField(max_length=100)
        account = models.CharField(max_length=100)
        plan = models.ForeignKey(Plan,on_delete=models.CASCADE)
# class Enquiry(models.Model):
#     user = 
#     related_property  = 
