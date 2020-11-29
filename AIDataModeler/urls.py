from . import views
from django.urls import path

urlpatterns = [
    path("", views.DayList.as_view(), name ='home'),   
    path('<slug:slug>/', views.DayDetails.as_view(), name='sentiment_details')
]