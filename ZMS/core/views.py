from django.shortcuts import render,HttpResponseRedirect
from .models import ticket_price_model
from .forms import feedbackform
from django.contrib import messages
from adminuser.models import Animalsmodel
# Create your views here.

def home(request):
    title='home'
    return render(request,'core/home.html',{'title':title})


def ticket_cost(request):
    title='ticket cost'
    types=ticket_price_model.objects.all()
    return render(request,'core/ticketcost.html',{'title':title,'types':types})

def feedback(request):
    title='Feedback'
    if request.method=="POST":
        fm=feedbackform(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Feedback Submitted Successfully !!!')
    else:
        fm=feedbackform()
    return render(request,'core/feedback.html',{'title':title,'form':fm})



def showavailableanimals(request):
    title='Available Animals'
    if request.method=="POST":
        item=request.POST['search']
        animals=Animalsmodel.objects.filter(name__icontains=item)
        acount=animals.count()
        return render(request,'core/showavailableanimals.html',{'animals':animals,'title':title,'acount':acount})
    else:
        animals=Animalsmodel.objects.all()
        return render(request,'core/showavailableanimals.html',{'animals':animals,'title':title})