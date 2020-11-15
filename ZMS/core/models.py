from django.db import models

# Create your models here.
class ticket_price_model(models.Model):
    ttype=models.CharField(max_length=70)
    tprice=models.IntegerField()

class feedbackmodel(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField()
    fdback=models.TextField()