from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout
from django.contrib import messages
from django.http import HttpResponse
from . forms import *
from . models import *

def regs(request):
    if request.method=='POST':
        f_name=request.POST['fname']
        usernm=request.POST['uname']
        email=request.POST['email']
        psw='sample'
        st=request.POST['marital_status']
        rg=regng(request.POST)
        if rg.is_valid():
            r=rg.save(commit=False)
        if User.objects.filter(username=usernm).exists():
            object = User.objects.get(username=usernm)
            object.first_name=f_name
            object.email=email
            user=auth.authenticate(username=usernm,password=psw)
            if user is not None:
                auth.login(request,user)
                object.save()
            job = rg.cleaned_data['job']
            age=rg.cleaned_data['age']
            district=rg.cleaned_data['district']
            place=rg.cleaned_data['place']
            marital_status=st
            currentuser=request.user
            modelba=regddd.objects.get(user=currentuser)
            modelba.job=job
            modelba.age=age
            modelba.district=district
            modelba.place=place
            modelba.ct=marital_status
            modelba.save()

            # regddd.objects.filter(user=usernm).  save(age=age,job=job,district=district,place=place,ct=marital_status)
            return redirect('reg:spouse')
        else:
            global u
            u=User.objects.create_user(username=usernm,password=psw,first_name=f_name,email=email)
            u.save()
            r.user=u
            r.ct=st
            r.save()

            user=auth.authenticate(username=usernm,password=psw)
            if user is not None:
                auth.login(request,user)
                if(r.ct=='MARRIED'):
                    return redirect('reg:spouse')
                else:
                    return redirect('reg:pay')
    return render(request,'home/registration.html')


def further(request):
    if request.method=='POST':
        w=wf(request.POST)
        if w.is_valid():
            ww=w.save(commit=False)
            # if wife.objects.filter(user=request.user).exists:
            #     current_user = request.user 
            #     wife_data=wife.objects.get(user=current_user)
            #     wife_data.nm = w.cleaned_data['nm']
            #     wife_data.ph=w.cleaned_data['ph']
            #     wife_data.pro=w.cleaned_data['pro']
            #     wife_data.age=w.cleaned_data['age']
            #     children=w.cleaned_data['children']
            #     wife_data.children=children
            #     wife_data.save()
            #     if(children>=0):
            #         return redirect('reg:child')
            #     else:
            #         return redirect('reg:pay')
    
            ww.user=request.user
            ww.save()
            if(ww.children>=0):
                return redirect('reg:child')
            else:
                return redirect('reg:pay')
    return render(request,'home/register_further.html')

def studs(request):
    if request.method=='POST':
        val=request.POST['kidreg']
        w=kid(request.POST)
        if w.is_valid():
            ww=w.save(commit=False)
            ww.user=request.user
            ww.save()
            if(val=='yes'):
                return redirect('reg:child')
            else:
                return redirect('reg:pay')
        else:
            return redirect('reg:pay')   
            
    return render(request,'home/studs.html')

def pay(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method=='POST':
        return redirect('reg:success')
    return render(request,'home/payment.html')

def thanks(request):
    return render(request, 'home/thank_you.html')

