from django.shortcuts import redirect, render
from django.views import generic
from professional.models import *
from home.models import *
from django.contrib.auth.models import User

# Create your views here.

class HomePageView(generic.ListView):
    # model:regddd
    template_name='dashboard/report1.html'
    context_object_name='registrants_dat'

    def get_queryset(self):
        return regddd.objects.order_by('district')

class SpousePageView(generic.ListView):
    # model:regddd
    template_name='dashboard/report2.html'
    context_object_name='spouse_dat'

    def get_queryset(self):
        return regddd.objects.order_by('district')

    # totalusers=User.objects.all()
    # personaldata=regddd.objects.all()
    # context = {
    #     'us':totalusers,
    #     'per':personaldata,
    # }
    # return render(request, 'dashboard/report1.html',context)
