from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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
  all_days = DaySentimentData.objects.all()
  context = {
    'days': days
  }
  return render(request, 'graph.html', context)

def About(request):
  return render(request, 'about.html')

def Policy(request):
  return render(request, 'policy.html')

def Contact(request):
  return render(request, 'contatct.html')

