from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


REG_CHOICE=(
    ('NOTHING','NOT REGISTERED'),
    ('ALONE','REGISTERED ALONE'),
    ('FAMILY','REGISTERED WITH FAMILY'),
    ('FRIENDS', 'REGISTERED WITH FRIENDS'),
    ('ONLINE', 'REGISTERED BUT VIEW ONLINE'))

PR_CHOICE=(
    ('INSTALLED','INSTALLED'),
    ('NOT','NOT INSTALLED'),
    ('ALREADY', 'ALREADY INSTALLED'))

class BasicForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=['username','first_name','password1', 'password2']
        labels={
            'username':'USERNAME',
            'first_name':'FULL NAME',
            'password1':'PASSWORD',
            'password2':'CONFIRM PASSWORD',}

        def clean(self):
            if User.objects.filter(username=self.cleaned_data['username']).exists():
                raise forms.ValidationError("Username is not unique")
        
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['username'].label = 'User ID'
            self.fields['first_name'].label = 'First Name'


class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)




class Unit(forms.ModelForm):
    class Meta:
        model=unitdata
        fields=['phone', 'district', 'zone', 'unit']
        labels={
            'phone':'PHONE',
            'district' : 'DISTRICT',
            'zone':'ZONE',
            'unit':'UNIT',
        }

class ProForm(forms.ModelForm):
    class Meta:
        model=prodir
        fields=[
            'name', 'jobsector', 'phone', 'workplace', 'reg_status', 'pr_status'
        ]
        widgets={
            'reg_status':forms.Select(choices= REG_CHOICE), 
            'pr_status':forms.Select(choices = PR_CHOICE),
            }