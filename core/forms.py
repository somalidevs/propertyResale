from django import forms
from .models import *
from accounts.models import Customer
from django.core.exceptions import ValidationError



CHOICES = [('Awash', 'Awash'), ('Commercial', 'Commercial'),('Bunna', 'Bunna'),('Dashen', 'Dashen'),]
choice  = [('Awsh(134252342)', 'Awsh(134252342)'), ('CBE(2342352342)', 'CBE(2342352342)'),('Bunna(23423352342)', 'Bunna(23423352342)'),('DSHN(24243235243)', 'DSHN(24243235243)'),]
class BankForm(forms.ModelForm):
    bank_name = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=CHOICES)
    account = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=choice)
    class Meta:
        model = EnquiryPlan
        fields = ['bank_name','account']


class CustomerEditForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields='__all__'
        
        
    def clean_fullname(self):
        fullname = self.cleaned_data.get('fullname')
        fullname_ = Customer.objects.filter(fullname=fullname)
        if fullname == fullname_:
            raise ValidationError('A user with that name already exists')
        return fullname

class CreatePropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields='__all__'
        exclude  = ['author','date_created','data_updated','slug']


