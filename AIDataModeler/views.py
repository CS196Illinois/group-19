from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def DayList(request):
  days = DaySentimentData.objects.all()
  context = {
        'days': days
	}
  return render(request, 'index.html', context)

def DayDetails(request, date_str):
    day = DaySentimentData.objects.get(date_str=date_str)
    context = {
        'day': day
    }
    return render(request, 'day_details.html', context)