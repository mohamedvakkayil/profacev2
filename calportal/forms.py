from django import forms
from django.forms import fields, widgets
from .models import * 

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

class calform(forms.ModelForm):
    class Meta:
        model=caldir
        fields={'name', 'jobsector', 'phone', 'panchayat'}

class calstat(forms.ModelForm):
    class Meta:
        model=caldir
        fields={'reg_status', 'pr_status'}
        widgets={
            'reg_status':forms.Select(choices= REG_CHOICE), 
            'pr_status':forms.Select(choices = PR_CHOICE),
        }
class dash(forms.ModelForm):
    class Meta:
        model = caldir
        fields={'name', 'jobsector', 'phone', 'panchayat','reg_status', 'pr_status'}