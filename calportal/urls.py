from django.urls import path
  
# importing views from views..py
from .views import *
urlpatterns = [
    path('', DataCreateView.as_view(), name='Datacreate' ),
]