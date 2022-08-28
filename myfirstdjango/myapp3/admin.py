from django.contrib import admin

from django.contrib import admin
from .models import MyApp
from .models import Sug

class MyAppAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')

class MySug(admin.ModelAdmin):
    list_display = ('name', 'sug')

admin.site.register(MyApp, MyAppAdmin)
admin.site.register(Sug, MySug)    
