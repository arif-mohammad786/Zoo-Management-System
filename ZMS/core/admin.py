from django.contrib import admin
from .models import ticket_price_model,feedbackmodel
# Register your models here.
@admin.register(ticket_price_model)
class admin_ticket_price(admin.ModelAdmin):
    list_display=['id','ttype','tprice']


@admin.register(feedbackmodel)
class admin_feedback(admin.ModelAdmin):
    list_display=['id','name','email','fdback']