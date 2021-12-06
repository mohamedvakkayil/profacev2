from django.urls import path
from . import views 
  
# importing views from views..py
from .views import *
app_name='cal'

urlpatterns = [
    path('Datacreate/', DataCreateView.as_view(), name='Datacreate' ),
    path('2520/', DataListView.as_view(), name='DataList' ),
    # path('dataupdate/<slug:slug>', DataUpdateView.as_view(), name='Datacreate' ),
    path('login/', views.Login, name='login')
]