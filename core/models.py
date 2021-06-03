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
                return super().save(*args,**kwargs)


class Location(models.Model):
        name=models.CharField(max_length=100)

        def __str__(self):
                return self.name

class Category(models.Model):
        name=models.CharField(max_length=100)


class Plan(models.Model):
        name = models.CharField(max_length=100)
        price = models.CharField(max_length=10)
        slug = models.SlugField(blank=True,null=True)
        plan_list1 = models.CharField(max_length=100,blank=True,null=True) 
        plan_list2 = models.CharField(max_length=100,blank=True,null=True)


        def __str__(self):
                return self.name


        def save(self,*args,**kwargs):
                if self.name:
                        slug_gen = str(slugify(self.name))
                self.slug = slug_gen
                return super().save(*args,**kwargs)

       

# class Enquiry(models.Model):
#     user = 
#     related_property  = 

class EnquiryPlan(models.Model):
        user = models.ForeignKey(Customer,on_delete=models.CASCADE, blank=True,null=True)
        bank_name = models.CharField(max_length=100,blank=True,null=True)
        account = models.CharField(max_length=100,blank=True,null=True)
        plan = models.ForeignKey(Plan,on_delete=models.CASCADE, blank=True,null=True)
        checked = models.BooleanField(default=False)

        def __str__(self):
                return str(self.bank_name+" - "+ self.user.user.username)


class Logo(models.Model):
        user =  models.ForeignKey(User,on_delete=models.CASCADE)
        image = models.ImageField(upload_to='images')

