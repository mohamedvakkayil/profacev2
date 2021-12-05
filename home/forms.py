from django import forms
from django.forms import fields
from . models import *

class regng(forms.ModelForm):
    class Meta:
        model=regddd
        fields={'age','job','district','place'}

class wf(forms.ModelForm):
    class Meta:
        model=wife
        fields={'nm','ph','pro','age','children'}

class kid(forms.ModelForm):
    class Meta:
        model=st
        fields={'nm','age',}