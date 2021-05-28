from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User






class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username','email','password1')


    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Self.User.username == username:
            raise forms.ValidationError('This username is already taken ')
        return username

