from . import views
from django.urls import path
import datetime

urlpatterns = [
    path("", views.DayList, name ='home'),   
    path("<slug:date_str>/", views.DayDetails, name='sentiment_details')
]