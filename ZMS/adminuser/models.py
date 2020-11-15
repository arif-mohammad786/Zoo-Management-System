from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import datetime
# Create your models here.
class Animalsmodel(models.Model):
    name=models.CharField(max_length=255)
    image=models.FileField()
    cage=models.IntegerField()
    breed=models.CharField(max_length=255)
    desc=models.TextField()

    
@receiver(post_delete,sender=Animalsmodel)
def delete_uploaded(sender,instance,**kwargs):
    instance.image.delete(False)


class Employeesmodel(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.TextField()
    image=models.FileField()


@receiver(post_delete,sender=Employeesmodel)
def delete_uploaded(sender,instance,**kwargs):
    instance.image.delete(False)


class Normal_ticket_model(models.Model):
    adult=models.IntegerField()
    children=models.IntegerField()
    date=models.DateField(default=datetime.date.today())
    total=models.IntegerField()


class Foreigners_ticket_model(models.Model):
    adult=models.IntegerField()
    children=models.IntegerField()
    date=models.DateField(default=datetime.date.today())
    total=models.IntegerField()