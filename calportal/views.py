from django import forms
from django.forms import fields
from django.http import request
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from .forms import calform, calstat, dash
from .models import caldir
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User,auth
from django.views.generic.list import ListView


class DataCreateView(LoginRequiredMixin, CreateView):
    login_url='cal:login'

    model = caldir
    form_class = calform
    template_name = 'calportal/enter.html'
    # fields = ['name', 'jobsector', 'phone', 'panchayat', 'reg_status', 'pr_status']

    def post(self, request, *args, **kwargs):
        caldata=calform(request.POST)
        if caldata.is_valid():
            cal = caldata.save(commit=False)
            cal.user = request.user
            cal.save()
        return redirect('cal:DataList')

class DataListView(LoginRequiredMixin, ListView):
    model = caldir
    paginate_by = 30
    template_name='calportal/listing.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
    # def get_absolute_url(self):
    #     qs=super(DataListView, self).get_queryset()
    #     return render(request, DataUpdateView/qs.filter(list=self.kwargs.get('phone'))

# class DataUpdateView(LoginRequiredMixin, kwargs=name, UpdateView):
#     login_url='login/'

#     model = caldir
#     form_class = dash
#     template_name = 'calportal/enter.html'
#     # fields = ['name', 'jobsector', 'phone', 'panchayat']

#     def post(self, request, *args, **kwargs):
#         caldata=calform(request.POST)
#         if caldata.is_valid():
#             cal = caldata.save(commit=False)
#             cal.user = request.user
#             cal.save()
#         return redirect('/')

def Login(request):
    if request.method=='POST':
        usernm=request.POST['phone']
        psw='sample'
        user=auth.authenticate(username=usernm,password=psw)
        if user is not None:
                auth.login(request,user)
        return redirect('cal:DataList')
    return render(request, 'calportal/login.html')
