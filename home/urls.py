from django.urls import path

from . import views

app_name= 'reg' 
urlpatterns = [
	path('',views.regs,name=''),
	path('spouse/',views.further,name='spouse'),
	path('child/',views.studs,name='child'),
	path('thanks/', views.thanks, name='success'),
	path('pay/', views.pay, name='pay'),

]
