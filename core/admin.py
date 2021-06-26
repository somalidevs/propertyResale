from django.contrib import admin

# Register your models here.
from core.models import *

admin.site.register(Property)
admin.site.register(Plan)
admin.site.register(Category)
admin.site.register(Location)
# admin.site.register(BankAccount)
admin.site.register(Logo)
admin.site.register(EnquiryPlan)
admin.site.register(Subscription)
admin.site.register(Type)
admin.site.register(ContactUs)
admin.site.register(Enquiry)