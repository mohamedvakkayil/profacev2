"""greenly_shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from .views import *

app_name = 'dash'

urlpatterns = [
	path('main',HomePageView.as_view(),name='das1'),
    path('spouse',SpousePageView.as_view(),name='das2'),
    path('csv', views.export_registrations_xls, name='export_registrations_xls'),
    path('csv2', views.export_spouse_xls, name='export_spouse_xls'),
]