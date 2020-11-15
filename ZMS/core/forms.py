from .models import feedbackmodel
from django import forms

class feedbackform(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(feedbackform,self).__init__(*args,**kwargs)
        self.label_suffix=' '
    class Meta:
        model=feedbackmodel
        fields="__all__"
        labels={'name':'Full Name','email':'Email ID','fdback':'Feedback'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'fdback':forms.Textarea(attrs={'class':'form-control','rows':3}),
        }