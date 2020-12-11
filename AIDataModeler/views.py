from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.core import serializers

# Create your views here.

def DayList(request):
  all_days = DaySentimentData.objects.all()

  paginator = Paginator(all_days, 3)  # 3 posts in each page
  page = request.GET.get('page')
  try:
      days = paginator.page(page)
  except PageNotAnInteger:
      days = paginator.page(1)
  except EmptyPage:
        days = paginator.page(paginator.num_pages)

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

def DayGraph(request):
  days = DaySentimentData.objects.all()
  context = {
    'days': days
  }
  return render(request, 'graph.html', context)

def DayGraphJson(request):
    days = DaySentimentData.objects.all()
    json_data = serializers.serialize('json', days, 
      use_natural_foreign_keys=True, use_natural_primary_keys=True)
    return HttpResponse(json_data)

def About(request):
  return render(request, 'about.html')

def Policy(request):
  return render(request, 'policy.html')

def Contact(request):
  return render(request, 'contatct.html')

