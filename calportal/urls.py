from django.urls import path
from . import views 
  
# importing views from views..py
from .views import *

app_name='cal'

urlpatterns = [
    path('280/', DataCreateView.as_view(), name='Datacreate' ),
    path('391/', DataListView.as_view(), name='DataList' ),
]