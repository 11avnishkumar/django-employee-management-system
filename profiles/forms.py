from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile

class UserUpdateForm(forms.ModelForm):   
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class ProfileUpdateForm(ModelForm):
    
    class Meta:
        model = Profile
        exclude = ['user']
        fields = '__all__'