from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import *

# Create your views here.
def homeView(request):
    return HttpResponse("<h1>Hello World</h1>")

class DayList(generic.ListView):
  queryset = DaySentimentData.objects.order_by('-date')
  template_name = 'index.html'

class DayDetails(generic.DetailView):
    model = DaySentimentData
    template_name = 'post_detail.html'  