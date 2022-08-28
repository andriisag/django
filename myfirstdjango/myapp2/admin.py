from django.contrib import admin

from django.contrib import admin
from .models import MyApp
from .models import Cars

class MyAppAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')

class CarsAdmin(admin.ModelAdmin):
      list_display = ('name', 'color')

admin.site.register(MyApp, MyAppAdmin)
admin.site.register(Cars, CarsAdmin)   
