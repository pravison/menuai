from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Client, Domain

class TenantRegistrationForm(forms.Form):
    tenant_name = forms.CharField(max_length=150)
    superuser_username = forms.CharField(max_length=150)
    superuser_email = forms.EmailField()
    superuser_password1 = forms.CharField(widget=forms.PasswordInput)
    superuser_password2 = forms.CharField(widget=forms.PasswordInput)
    phone_number = forms.CharField(max_length=16)


    


