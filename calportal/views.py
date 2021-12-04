from django import forms
from django.forms import fields
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import calform, calstat, dash
from .models import caldir

class DataCreateView(CreateView):
    model = caldir
    form_class = calform
    template_name = 'calportal/enter.html'
    # fields = ['name', 'jobsector', 'phone', 'panchayat']

# Create your views here.
