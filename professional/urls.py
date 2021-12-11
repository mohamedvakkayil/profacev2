from django.urls import path
from . import views
from .views import *

app_name = 'pro'

urlpatterns = [
	path('987/', SignUp.as_view(),name='signup'),
	path('137/', UnitEntry.as_view(), name='unit'),
	path('808/', DataEntry.as_view(), name='dataentry'),
	path('778/', DataListView.as_view(), name='datalist'),
	path('110', views.login_page, name='log'),
	path('rotr/', router.as_view(), name='router'),
]