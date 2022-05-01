from django import forms
from django.forms import ModelForm
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .models import Employee,Upload_employee_details

class addEmployee(ModelForm):
    class Meta:
        model = Employee
        exclude = ['date','is_active']
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(addEmployee, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['class'] = 'form-control form-control-lg '
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['email'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['gender'].widget.attrs['class'] = 'form-select form-select-lg'
        self.fields['phoneno'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['phoneno'].widget.attrs['placeholder'] = 'Phone No'
        self.fields['country'].widget.attrs['class'] = 'form-select form-select-lg'
        self.fields['country'].widget.attrs['placeholder'] = 'Country'
        self.fields['state'].widget.attrs['class'] = 'form-select form-select-lg'
        self.fields['state'].widget.attrs['placeholder'] = 'State'
        self.fields['designation'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['designation'].widget.attrs['placeholder'] = 'Designation'
        self.fields['birthdate'].widget.attrs['class'] = 'form-control form-control-lg '
        self.fields['birthdate'].widget.attrs['placeholder'] = 'Date of Birth'
        self.fields['address'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['address'].widget.attrs['placeholder'] = 'Address'
        self.fields['address'].widget.attrs['rows'] = '3'

class Employee_uploaded_details(ModelForm):
    class Meta:
        model = Upload_employee_details
        fields = ('file_name',)
    def __init__(self, *args, **kwargs):
        super(Employee_uploaded_details, self).__init__(*args, **kwargs)
        self.fields['file_name'].widget.attrs['class'] = 'form-control form-control-lg'    