from django.contrib import admin
from .models import *
from django.contrib import admin
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['user', 'contact_number', 'comment']

admin.site.register(ContacUs, ContactAdmin)