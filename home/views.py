from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
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
            messages.info(request,'phone number already exist')
            return redirect('/')
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
                    return redirect('spouse')
                else:
                    return redirect('success')
    return render(request,'registration.html')


def further(request):
    if request.method=='POST':
        w=wf(request.POST)
        if w.is_valid():
            ww=w.save(commit=False)
            ww.user=request.user
            ww.save()
            if(ww.children>=0):
                return redirect('child')
            else:
                return redirect('success')
    return render(request,'register_further.html')

def studs(request):
    if request.method=='POST':
        val=request.POST['kidreg']
        w=kid(request.POST)
        if w.is_valid():
            ww=w.save(commit=False)
            ww.user=request.user
            ww.save()
            if(val=='yes'):
                return redirect('child')
            else:
                return redirect('success')
        else:
            return redirect('success')   
            
    return render(request,'studs.html')

def thanks(request):
    return render(request, 'thank_you.html')

