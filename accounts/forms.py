
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

CHOICES = CHOICES = [('male', 'male'), ('female', 'female')]
class ProfileUpdateForm(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phonenumber = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-control'}), choices=CHOICES)
    image = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':2, 'cols':35}))
    # gender = forms.CharField(widget=forms.Select)
    class Meta:
        model = Customer
        fields = "__all__"
        exclude = ['auth_token','blocked','role','is_verified','user']