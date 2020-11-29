from django.contrib import admin
from .models import *
# Register your models here.


class DaySentimentAdmin(admin.ModelAdmin):
    list_display = ['date']
    list_filter = ["date"]
    search_fields = ['date']
    #prepopulated_fields = {'slug': ('title',)}


class SentimentModelAdmin(admin.ModelAdmin):
    list_display = ['positivity', 'negativity']
    list_filter = ['positivity', 'negativity']
    search_fields = ['positivity', 'negativity']
    #prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(DaySentimentData, DaySentimentAdmin)
admin.site.register(SentimentModel, SentimentModelAdmin)
