from django.contrib import admin
from .models import *
# Register your models here.


class DaySentimentAdmin(admin.ModelAdmin):
    list_display = ['date']
    list_filter = ["date"]
    search_fields = ['date']
    #prepopulated_fields = {'slug': ('title',)}


class OutletSentimentAdmin(admin.ModelAdmin):
    list_display = ['cnn', 'politico', 'usa_today', 'upi', 'federalist', 
    'average', 'average_consevative', 'average_liberal']
    list_filter = ['cnn', 'politico', 'usa_today', 'upi', 'federalist', 
    'average', 'average_consevative', 'average_liberal']
    search_fields = ['cnn', 'politico', 'usa_today', 'upi', 'federalist', 
    'average', 'average_consevative', 'average_liberal']
    #prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(DaySentimentData, DaySentimentAdmin)
admin.site.register(OutletSentiment, OutletSentimentAdmin)
