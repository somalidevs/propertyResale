from django import forms
from .models import *
from accounts.models import Customer



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
        





