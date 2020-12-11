from . import views
from django.urls import path
import datetime

urlpatterns = [
    path("", views.DayList, name ='home'),   
    path("<slug:date_str>/", views.DayDetails, name='sentiment_details'),
    path("about", views.About, name="about" ),
    path("policy", views.Policy, name="policy" ),
    path("contact", views.Contact, name="contact" ),
    path("graph", views.DayGraph, name="day_graph"),
    path("api/graph", views.DayGraphJson, name="json_graph_request")
]