from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from professional.models import *
from home.models import *
from django.contrib.auth.models import User
import csv

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

def export_registrations_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="registration_data.xls"'

    registrants = regddd.objects.order_by('district')
    writer = csv.writer(response)  
    for registrant in registrants:
        writer.writerow([registrant.district, registrant.user.first_name,  registrant.job,registrant.user.username, registrant.place])
        

    return response 

def export_spouse_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="spouse_data.xls"'

    registrants = wife.objects.order_by('nm')
    writer = csv.writer(response)  
    for registrant in registrants:
        # writer.writerow([registrant.district, registrant.user.wife.nm,  registrant.user.wife.ph,registrant.user.first_name])
        writer.writerow([registrant.user.regddd.district, registrant.user.wife.nm, registrant.user.first_name ])

    return response 

def export_childrens_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="childrens_data.xls"'

    registrants = st.objects.order_by('nm')
    writer = csv.writer(response)  
    for registrant in registrants:
        # writer.writerow([registrant.district, registrant.user.wife.nm,  registrant.user.wife.ph,registrant.user.first_name])
        writer.writerow([registrant.user.regddd.district, registrant.nm, registrant.age, registrant.user.first_name ])

    return response 
    