from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Property)
admin.site.register(Plan)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(BankAccount)