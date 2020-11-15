from django.contrib import admin
from .models import Animalsmodel,Employeesmodel,Normal_ticket_model,Foreigners_ticket_model
# Register your models here.
@admin.register(Animalsmodel)
class adminanimal(admin.ModelAdmin):
    list_display=['id','name','image','cage','breed','desc']


@admin.register(Employeesmodel)
class adminemployee(admin.ModelAdmin):
    list_display=['id','name','email','phone','address','image']


@admin.register(Normal_ticket_model)
class adminnormalticket(admin.ModelAdmin):
    list_display=['id','adult','children','date','total']


@admin.register(Foreigners_ticket_model)
class adminforeignerticket(admin.ModelAdmin):
    list_display=['id','adult','children','date','total']