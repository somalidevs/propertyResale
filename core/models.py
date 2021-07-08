from django.db import models
from django.db.models.fields import TextField
import django_quill
from django_quill.fields import *
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.utils.text import slugify
from accounts.models import Customer
from django.db.models.signals import post_save
from django.conf import settings
import stripe
from django.urls import reverse
from django.core.validators import MinValueValidator,MaxValueValidator
stripe.api_key = settings.STRIPE_SECRET_KEY


class Type(models.Model):
        name = models.CharField(max_length=100)  
        def __str__(self):
            return self.name
class Location(models.Model):
        name=models.CharField(max_length=100)

        def __str__(self):
                return self.name

class Category(models.Model):
        name=models.CharField(max_length=100)

        def __str__(self):
            return self.name
    
STATUS=(('active','active'),('inactive','inactive'))
class Property(models.Model):
        name=models.CharField(max_length=100)
        author=models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True,null=True)
        price=models.CharField(max_length=20)
        slug = models.SlugField(blank=True,null=True)
        category=models.ForeignKey(Category,on_delete=models.CASCADE)
        brand = models.CharField(blank=True,null=True,max_length=100)
        ptype=models.ForeignKey(Type,on_delete=models.CASCADE)
        location=models.ForeignKey(Location,on_delete=models.CASCADE)
        score = models.IntegerField(default=0,validators=[MaxValueValidator(5),MinValueValidator(0)])
        images_1=models.ImageField(upload_to='images') 
        images_2=models.ImageField(upload_to='images',blank=True,null=True) 
        images_3=models.ImageField(upload_to='images',blank=True,null=True) 
        description=models.TextField(blank=True,null=True)
        status=models.CharField(max_length=10,choices=STATUS)
        date_created=models.DateTimeField(auto_now=True)
        date_updated=models.DateTimeField(auto_now_add=True)

        
        
        def __str__(self):
            return self.name
    
    
        def save(self,*args,**kwargs):
                if self.name:
                        slug_gen = str(slugify(self.name))
                self.slug = slug_gen
                return super().save(*args,**kwargs)
        
        
        def get_absolute_url(self):
            return reverse("property_detail_view", kwargs={"slug": self.slug})
        



class Plan(models.Model):
        name = models.CharField(max_length=100)
        price = models.CharField(max_length=10)
        slug = models.SlugField(blank=True,null=True)
        stripe_price_id = models.CharField(max_length=50,blank=True,null=True)
        currency = models.CharField(max_length=10,default='usd')
        plan_list1 = models.CharField(max_length=100,blank=True,null=True) 
        plan_list2 = models.CharField(max_length=100,blank=True,null=True)


        def __str__(self):
                return self.name


        def save(self,*args,**kwargs):
                if self.name:
                        slug_gen = str(slugify(self.name))
                self.slug = slug_gen
                return super().save(*args,**kwargs)

       

class Enquiry(models.Model):
    user = models.ForeignKey(Customer,on_delete=models.CASCADE)
    related_property  = models.ForeignKey(Property,on_delete=models.CASCADE)
    message = models.TextField()
    
    
    def __str__(self):
            return self.message[:5]



class EnquiryPlan(models.Model):
        user = models.ForeignKey(Customer,on_delete=models.CASCADE, blank=True,null=True)
        bank_name = models.CharField(max_length=100,blank=True,null=True)
        account = models.CharField(max_length=100,blank=True,null=True)
        plan = models.ForeignKey(Plan,on_delete=models.CASCADE, blank=True,null=True)
        checked = models.BooleanField(default=False)

        # def __str__(self):
        #         return str(self.bank_name+" - "+ self.user.user.username)


class Logo(models.Model):
        user =  models.ForeignKey(User,on_delete=models.CASCADE)              
        image = models.ImageField(upload_to='images')



class Subscription(models.Model):
        user = user = models.ForeignKey(Customer,on_delete=models.CASCADE)
        plan = models.ForeignKey(Plan,on_delete=models.CASCADE)
        created = models.DateTimeField(auto_now_add=True)
        stripe_subscription_id = models.CharField(max_length=50)
        status = models.CharField(max_length=100)


        def __str__(self):
                return self.user.user.email




def post_save_customer(sender,instance,created,*args,**kwargs):
        if created:
                free_trial_plan = Plan.objects.get(name="Free Trial")
                subscription = Subscription.objects.create(user=instance,plan=free_trial_plan)
                stripe_customer = stripe.Customer.create(email=instance.user.email)
                stripe_subscription = stripe.Subscription.create(
                        customer=stripe_customer['id'],
                        items=[{'price':'price_1IyVxWLkW4Uiu90UYQuxZF82'}],
                        trial_period_days = 7 
                )
                subscription.status = stripe_subscription["status"]
                subscription.stripe_subscription_id = stripe_subscription["id"]
                subscription.save()
                instance.stripe_customer_id = stripe_customer['id']
                instance.save()
        




post_save.connect(post_save_customer,sender=Customer)





class ContactUs(models.Model):
        name = models.CharField(max_length=100)
        subject = models.CharField(max_length=100) 
        email = models.EmailField()
        phone = models.CharField(max_length=100)
        message = models.TextField()
        
        
        def __str__(self):
                return self.name






