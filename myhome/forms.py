from pyexpat import model
# from attr import fields
from django import forms
from .models import *
from django.contrib.auth.models import User

class loginForm(forms.ModelForm):
    class Meta:
        model  = User
        fields = ['username','password']

class signupForm(forms.ModelForm):
    class Meta:
        model  = User
        fields = ['username','password','first_name','last_name','email']