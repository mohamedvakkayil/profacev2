from django.urls import path
from . import views
from .views import *

app_name = 'pro'

urlpatterns = [
	path('signup/', SignUp.as_view(),name='signup'),
	path('unit/', UnitEntry.as_view(), name='unit'),
	path('de/', DataEntry.as_view(), name='dataentry'),
	path('dl/', DataListView.as_view(), name='datalist'),
	path('', views.login_page, name='log'),
	path('roter/', views.router, name='router'),
]