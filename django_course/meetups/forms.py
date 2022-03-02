from django import forms

#from .models import Participant

class RegistrationForm(forms.Form):  #.ModelForm if u want to save an object
    #class Meta:
        #model = Participant for .ModelForm
        #fields = ['email']
    email = forms.EmailField(label='Your email')