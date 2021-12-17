from django.contrib.auth import authenticate , login, logout
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .forms import *
from .models import * 
from django.contrib.auth.models import User, auth
from django.contrib.auth.mixins import LoginRequiredMixin

def SignUp(request):
    if request.method=='POST':
        usernm = request.POST['username']
        password =request.POST['password']
        print(usernm,password)
        if User.objects.filter(username=usernm).exists():
            form = User.objects.get(username=usernm)
            form.set_password(password)
            form.save()
        else:
            new_user=User.objects.create_user(username=usernm,password=password,)
            new_user.save()
        
        user = authenticate(request, username=usernm, password=password)
        if user is not None:
            login(request, user)
        return redirect('pro:unit')

    return render(request, 'professional/signup.html')

# class SignUp(CreateView):
#     form_class=BasicForm
#     template_name='professional/signup.html'
#     success_url = 'unit'

#     def form_valid(self, form):
#         usernm = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#         if User.objects.filter(username=usernm).exists():
#             object = User.objects.get(username=usernm)
#             object.password=password
#         form.save()
        # user = authenticate(username=usernm, password=password,)
        # login(self.request, user)
        # return redirect('pro:unit')

class UnitEntry(LoginRequiredMixin, CreateView):
    login_url='pro:log'
    
    models=unitdata
    form_class=Unit
    template_name='professional/next.html'

    def post(self, request, *args, **kwargs):
        unitdata1=Unit(request.POST)
        if unitdata1.is_valid():
            conunit = unitdata1.save(commit=False)
            conunit.user = request.user
            conunit.save()
        return redirect('pro:datalist')




def login_page(request):
    if request.method=='POST':
        usernm=request.POST['username']
        psw=request.POST['password']
        user=auth.authenticate(username=usernm,password=psw)
        if user is not None:
            auth.login(request,user)
            return redirect('pro:datalist')
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
    login_url='pro:log'

    model=prodir
    paginate_by=30
    template_name='professional/list.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class router(LoginRequiredMixin, TemplateView):
    login_url='pro:log'

    template_name = 'professional/router.html'