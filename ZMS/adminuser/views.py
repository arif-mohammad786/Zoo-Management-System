from django.shortcuts import render,HttpResponseRedirect
from .forms import loginform,animalsform,ticket_price_form,passwordchangecustomform,Employees_form,Normal_ticket_form
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Animalsmodel,Employeesmodel,Normal_ticket_model,Foreigners_ticket_model
from core.models import feedbackmodel,ticket_price_model
import datetime
contact_email="admin@gmail.com"
contact_phone="9999999999"
about_details="Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ea, ex sed. Neque nisisimilique explicabo soluta repellendus pariatur enim. Eius ad dignissimos odiovel numquam rerum enim beatae repellat quo!pariatur enim. Eius ad dignissimos odio"
child_price=0
adult_price=0
childrens=0
adults=0
# Create your views here.

def about(request):
    title='About Us'
    return render(request,'adminuser/aboutus.html',{'title':title,'about_details':about_details})


def contact(request):
    title='Contact Us'
    return render(request,'adminuser/contactus.html',{'title':title,'email':contact_email,'phone':contact_phone})



def admin_login(request):
    title='Login'
    if request.user.is_authenticated:
        return HttpResponseRedirect('/adminuser/dashboard/')
    else:
        if request.method=="POST":
            fm=loginform(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user != None:
                    login(request,user)
                    return HttpResponseRedirect('/adminuser/dashboard/')

        else:
            fm=loginform()
    return render(request,'adminuser/adminlogin.html',{'title':title,'form':fm})


def logoutfunction(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


def dashboard(request):
    if request.user.is_authenticated:
        page='Dashboard'
        animals=Animalsmodel.objects.all()
        feedbacks=feedbackmodel.objects.all()
        employees=Employeesmodel.objects.all()
        ntickets=Normal_ticket_model.objects.filter(date=datetime.date.today())
        ftickets=Foreigners_ticket_model.objects.filter(date=datetime.date.today())
        total_today=ntickets.union(ftickets)
        today=datetime.date.today()
        yesterday=today-datetime.timedelta(days=1)
        ntickets=Normal_ticket_model.objects.filter(date=yesterday)
        ftickets=Foreigners_ticket_model.objects.filter(date=yesterday)
        tickets=ntickets.union(ftickets)
        return render(request,'adminuser/dashboard.html',{'page':page,'animals':animals.count(),'feedbacks':feedbacks.count(),
        'employees':employees.count(),'today_tickets':total_today.count(),'yesterday_tickets':tickets.count()})
    else:
        return HttpResponseRedirect('/adminuser/adminlogin/')

def addanimal(request):
    if request.user.is_authenticated:
        page='Add Animal'
        if request.method=="POST":
            fm=animalsform(request.POST,request.FILES)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Animal Added Successfully !!!')
        else:
            fm=animalsform()
        return render(request,'adminuser/addanimal.html',{'page':page,'form':fm})
    else:
        return HttpResponseRedirect('/adminuser/adminlogin/')


def availableanimals(request):
    if request.user.is_authenticated:
        page='Available Animals'
        animals=Animalsmodel.objects.all()
        return render(request,'adminuser/availableanimals.html',{'page':page,'animals':animals})
    else:
        return HttpResponseRedirect('/adminuser/adminlogin/')


def updateanimal(request,id):
    if request.user.is_authenticated:
        page='Update Animal'
        pi=Animalsmodel.objects.get(pk=id)
        if request.method=="POST":
            fm=animalsform(request.POST,request.FILES,instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Animal Details Updated Successfully !!!')
        else:
            fm=animalsform(instance=pi)
            return render(request,'adminuser/editanimal.html',{'page':page,'form':fm,'url':pi.image.url})
        return render(request,'adminuser/editanimal.html',{'page':page,'form':fm})
    else:
        return HttpResponseRedirect('/adminuser/adminlogin/')
    

def deleteanimal(request,id):
    if request.user.is_authenticated:
        pi=Animalsmodel.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/adminuser/availableanimals/')
    else:
        return HttpResponseRedirect('/adminuser/adminlogin/')
    

def ticket_types(request):
    if request.user.is_authenticated:
        page='Ticket Types'
        types=ticket_price_model.objects.all()
        return render(request,'adminuser/tickettypes.html',{'page':page,'types':types})  
    else:
        return HttpResponseRedirect('/adminuser/adminlogin/')

def edit_ticket_type(request,id):
    if request.user.is_authenticated:
        page='Update Ticket Types'
        pi=ticket_price_model.objects.get(pk=id)
        if request.method=="POST":
            fm=ticket_price_form(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Ticket Price Updated Successfully !!!')
        else:
            fm=ticket_price_form(instance=pi)
        return render(request,'adminuser/edittickettype.html',{'page':page,'form':fm})
    else:
        return HttpResponseRedirect('/adminuser/adminlogin/')



def feedbacks(request):
    if request.user.is_authenticated:
        page='Manage Feedbacks'
        feedbacks=feedbackmodel.objects.all()
        return render(request,'adminuser/feedbacks.html',{'page':page,'feedbacks':feedbacks})  
    else:
        return HttpResponseRedirect('/adminuser/adminlogin/')


def delete_feedback(request,id):
    if request.user.is_authenticated:
        pi=feedbackmodel.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/adminuser/feedback/')
    else:
        return HttpResponseRedirect('/adminuser/adminlogin/')


def change_password(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=passwordchangecustomform(data=request.POST,user=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Password Changed Successfully !!!')
        else:
            fm=passwordchangecustomform(user=request.user)
        return render(request,'adminuser/changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/adminuser/adminlogin/')
    

def update_contact_details(request):
    if request.user.is_authenticated:
        page='Update Contact Details'
        if request.method=="POST":
            newemail=request.POST['newemail']
            newphone=request.POST['newphone']
            global contact_email
            contact_email=newemail
            global contact_phone
            contact_phone=newphone
            messages.success(request,'Contact Details Updated Successfully !!!')
        return render(request,'adminuser/updatecontactdetails.html',{'page':page,'email':contact_email,'phone':contact_phone})
    else:
        return HttpResponseRedirect('/adminuser/adminlogin/')



def update_about_details(request):
    if request.user.is_authenticated:
        page='Update About Details'
        if request.method=="POST":
            newdetails=request.POST['newdetails']
            global about_details
            about_details=newdetails
            messages.success(request,'About Details Updated Successfully !!!')
        return render(request,'adminuser/updateaboutdetails.html',{'page':page,'about_details':about_details})
    else:
        return HttpResponseRedirect('/adminuser/adminlogin/')
    

def add_new_employee(request):
    if request.user.is_authenticated:
        page='Add New Employee'
        if request.method=="POST":
            fm=Employees_form(request.POST,request.FILES)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Employee Added Successfully !!!')
        else:   
            fm=Employees_form()
        return render(request,'adminuser/addemployee.html',{'page':page,'form':fm})
    else:
        return HttpResponseRedirect('/adminuser/adminlogin/')

def show_available_employees(request):
    if request.user.is_authenticated:
        page='Available Employees'
        employees=Employeesmodel.objects.all()
        return render(request,'adminuser/availableemployees.html',{'page':page,'employees':employees})
    else:
        return HttpResponseRedirect('/adminuser/adminlogin/')


def delete_employee(request,id):
    if request.user.is_authenticated:
        pi=Employeesmodel.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/adminuser/availableemployees/')
    else:
        return HttpResponseRedirect('/adminuser/adminlogin/')



def update_employee(request,id):
    if request.user.is_authenticated:
        page='Update Employee'
        pi=Employeesmodel.objects.get(pk=id)
        if request.method=="POST":
            fm=Employees_form(request.POST,request.FILES,instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Employee Details Updated Successfully !!!')
        else:
            fm=Employees_form(instance=pi)
            return render(request,'adminuser/editemployee.html',{'page':page,'form':fm,'url':pi.image.url})
        return render(request,'adminuser/editemployee.html',{'page':page,'form':fm})
    else:
        return HttpResponseRedirect('/adminuser/adminlogin/')


def normal_ticket(request):
    if request.user.is_authenticated:
        page='Normal Ticket'
        if request.method=="POST":
            fm=Normal_ticket_form(request.POST)
            if fm.is_valid():
                pi=ticket_price_model.objects.get(ttype='Normal Adult')
                qi=ticket_price_model.objects.get(ttype='Normal Child')
                global child_price
                child_price=qi.tprice
                global adult_price
                adult_price=pi.tprice
                global adults
                adults=int(request.POST['adult'])
                global childrens
                childrens=int(request.POST['children'])
                total=(adults*adult_price)+(childrens*child_price)
                ticket=Normal_ticket_model(adult=adults,children=childrens,total=total)
                ticket.save()
                return HttpResponseRedirect('/adminuser/printticket/')
                
        else:
            fm=Normal_ticket_form()
        return render(request,'adminuser/normalticket.html',{'form':fm,'page':page})
    else:
        return HttpResponseRedirect('/adminuser/adminlogin/')

def print_ticket(request):
    if request.user.is_authenticated:
        total_adult_price=adult_price*adults
        total_child_price=child_price*childrens
        total=total_adult_price+total_child_price
        return render(request,'adminuser/printticket.html',{'child_price':child_price,'adult_price':adult_price,
        'childrens':childrens,'adults':adults,'datetime':datetime.datetime.today(),'total':total})
    else:
        return HttpResponseRedirect('/adminuser/adminlogin/')


def show_normal_tickets(request):
    if request.user.is_authenticated:
        page='Manage Normal Tickets'
        tickets=Normal_ticket_model.objects.all()
        return render(request,'adminuser/shownormalticket.html',{'tickets':tickets,'page':page})
    else:
        return HttpResponseRedirect('/adminuser/adminlogin/')

def delete_normal_ticket(request,id):
    if request.user.is_authenticated:
        pi=Normal_ticket_model.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/adminuser/shownormalticket/')
    else:
        return HttpResponseRedirect('/adminuser/adminlogin/')

def foreigners_ticket(request):
    if request.user.is_authenticated:
        page='Foreigners Ticket'
        if request.method=="POST":
            fm=Normal_ticket_form(request.POST)
            if fm.is_valid():
                pi=ticket_price_model.objects.get(ttype='Foreigner Adult')
                qi=ticket_price_model.objects.get(ttype='Foreigner Child')
                global child_price
                child_price=qi.tprice
                global adult_price
                adult_price=pi.tprice
                global adults
                adults=int(request.POST['adult'])
                global childrens
                childrens=int(request.POST['children'])
                total=(adults*adult_price)+(childrens*child_price)
                ticket=Foreigners_ticket_model(adult=adults,children=childrens,total=total)
                ticket.save()
                return HttpResponseRedirect('/adminuser/printticket/')
                
        else:
            fm=Normal_ticket_form()
        return render(request,'adminuser/normalticket.html',{'form':fm,'page':page})
    else:
        return HttpResponseRedirect('/adminuser/adminlogin/')


def show_foreigners_tickets(request):
    if request.user.is_authenticated:
        page='Manage Foreigners Tickets'
        tickets=Foreigners_ticket_model.objects.all()
        return render(request,'adminuser/showforeignersticket.html',{'tickets':tickets,'page':page})
    else:
        return HttpResponseRedirect('/adminuser/adminlogin/')
    

def delete_foreigners_ticket(request,id):
    if request.user.is_authenticated:
        pi=Foreigners_ticket_model.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/adminuser/showforeignersticket/')
    else:
        return HttpResponseRedirect('/adminuser/adminlogin/')
    
def show_today_tickets(request):
    if request.user.is_authenticated:
        page='Today\'s Tickets'
        ntickets=Normal_ticket_model.objects.filter(date=datetime.date.today())
        ftickets=Foreigners_ticket_model.objects.filter(date=datetime.date.today())
        tickets=ntickets.union(ftickets)
        return render(request,'adminuser/showtodaytickets.html',{'page':page,'tickets':tickets})
    else:
        return HttpResponseRedirect('/adminuser/adminlogin/')
    


def show_yesterday_tickets(request):
    if request.user.is_authenticated:
        page='Yesterday\'s Tickets'
        today=datetime.date.today()
        yesterday=today-datetime.timedelta(days=1)
        ntickets=Normal_ticket_model.objects.filter(date=yesterday)
        ftickets=Foreigners_ticket_model.objects.filter(date=yesterday)
        tickets=ntickets.union(ftickets)
        return render(request,'adminuser/showyesterdaytickets.html',{'page':page,'tickets':tickets})
    else:
        return HttpResponseRedirect('/adminuser/adminlogin/')
