from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, View
from django.views.generic.list import ListView
from .forms import *
from .models import * 
from django.contrib.auth.models import User, auth
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUp(CreateView):
    form_class=BasicForm
    template_name='professional/signup.html'
    success_url = 'unit'

    def form_valid(self, form):
        form.save()
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'],)
        login(self.request, user)
        return redirect('pro:unit')

class UnitEntry(LoginRequiredMixin, CreateView):
    login_url='pro:log'
    
    models=unitdata
    form_class=Unit
    template_name='professional/next.html'

    def post(self, request, *args, **kwargs):
        unitdata=Unit(request.POST)
        if unitdata.is_valid():
            conunit = unitdata.save(commit=False)
            conunit.user = request.user
            conunit.save()
        return redirect('pro:router')




def login_page(request):
    if request.method=='POST':
        usernm=request.POST['username']
        psw=request.POST['password']
        user=auth.authenticate(username=usernm,password=psw)
        if user is not None:
            auth.login(request,user)
            return redirect('pro:router')
    return render(request,'professional/login.html')

class DataEntry(LoginRequiredMixin, CreateView):
    login_url='pro:log'

    model = prodir
    form_class = ProForm
    template_name='professional/update.html'
    # fields = ['name', 'jobsector', 'phone', 'panchayat', 'reg_status', 'pr_status']

    def post(self, request, *args, **kwargs):
        prodat=ProForm(request.POST)
        if prodat.is_valid():
            cal = prodat.save(commit=False)
            cal.user = request.user
            cal.save()
        return redirect('pro:datalist')


class DataListView(LoginRequiredMixin, ListView):
    model=prodir
    paginate_by=30
    template_name='professional/list.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


def router(request):
    return render(request, 'professional/router.html')