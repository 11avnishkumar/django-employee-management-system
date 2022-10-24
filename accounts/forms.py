from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class registerUser(UserCreationForm):
    email = forms.EmailField(error_messages={'required':'Email Required'},widget=forms.EmailInput(attrs={'class': 'py-3 px-2 w-full rounded-lg border border-slate-300 focus:border-slate-600 focus:outline-none', 'placeholder': 'Email'}))
    first_name = forms.CharField(error_messages={'required':'First Name required'},max_length=60, widget=forms.TextInput(attrs={'class': 'py-3 px-2 w-full rounded-lg border border-slate-300 focus:border-slate-600 focus:outline-none', 'placeholder': 'First Name'}))
    last_name = forms.CharField(error_messages={'required':'Last Name required'},max_length=60, widget=forms.TextInput(attrs={'class': 'py-3 px-2 w-full rounded-lg border border-slate-300 focus:border-slate-600 focus:outline-none', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(registerUser, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'py-3 px-2 w-full rounded-lg border border-slate-300 focus:border-slate-600 focus:outline-none'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['class'] = 'py-3 px-2 w-full rounded-lg border border-slate-300 focus:border-slate-600 focus:outline-none'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'py-3 px-2 w-full rounded-lg border border-slate-300 focus:border-slate-600 foucus:ring ring-slate-600 focus:outline-none'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

