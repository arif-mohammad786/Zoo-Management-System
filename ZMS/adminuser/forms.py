from django import forms
from django.contrib.auth.forms import AuthenticationForm,UsernameField,PasswordChangeForm
from django.utils.translation import gettext,gettext_lazy as _
from .models import Animalsmodel,Employeesmodel,Normal_ticket_model
from core.models import ticket_price_model

class loginform(AuthenticationForm):
    username=UsernameField(label_suffix=" ",widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label_suffix=" ",label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


class animalsform(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(animalsform,self).__init__(*args,**kwargs)
        self.label_suffix=' '
    class Meta:
        model=Animalsmodel
        fields="__all__"
        labels={
            'name':'Animal Name','image':'Animal Image','cage':'Cage Number','breed':'Breed','desc':'Description'
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Animal Name'}),
            'image':forms.FileInput(attrs={'class':'form-control-file'}),
            'cage':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Cage Number'}),
            'breed':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Animal Breed'}),
            'desc':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Animal Description','rows':3}),

        }
    
class ticket_price_form(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ticket_price_form,self).__init__(*args,**kwargs)
        self.label_suffix=' '
    class Meta:
        model=ticket_price_model
        fields="__all__"
        labels={
            'ttype':'Ticket Type','tprice':'Ticket Price in Rs'
        }
        widgets={
            'ttype':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
            'tprice':forms.NumberInput(attrs={'class':'form-control'})
        }



class passwordchangecustomform(PasswordChangeForm):
    def __init__(self,user,*args,**kwargs):
        super(passwordchangecustomform,self).__init__(user,*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
        
    
   
class Employees_form(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(Employees_form,self).__init__(*args,**kwargs)
        self.label_suffix=' '
    class Meta:
        model=Employeesmodel
        fields="__all__"
        labels={
            'name':'Full Name','email':'Email ID','phone':'Phone Number','address':'Current Address','image':'Upload Employee\'s Image'
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Full Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}),
            'phone':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Phone Number'}),
            'address':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Complete Address','rows':3}),
            'image':forms.FileInput(attrs={'class':'form-control-file','placeholder':'Upload Recenet Photo'}),

        }
    
class Normal_ticket_form(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(Normal_ticket_form,self).__init__(*args,**kwargs)
        self.label_suffix=' '
    class Meta:
        model=Normal_ticket_model
        exclude=('date','total')
        labels={
            'adult':'Adult','children':'Children','total':'Total Price'
        }
        widgets={
            'adult':forms.NumberInput(attrs={'class':'form-control','placeholder':'No. Of Adults'}),
            'children':forms.NumberInput(attrs={'class':'form-control','placeholder':'No. of Children'}),

        }