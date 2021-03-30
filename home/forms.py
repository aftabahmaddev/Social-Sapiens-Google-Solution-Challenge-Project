from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import UserCreationForm
from .models import post 
class post_form(forms.ModelForm):
    class Meta:
        model= post
        fields = '__all__'
        
        widgets={
            
            'email': forms.EmailInput( attrs={'class':'text','placeholder':'email if possible'}),
            'name': forms.TextInput( attrs={'class':'text','required':'True', 'placeholder':'Name of person to help'}),
            'about_payment': forms.TextInput( attrs={'class':'text', 'placeholder':'Bank account, easy paisa or any other'}),
            'phone': forms.TextInput( attrs={'class':'text', 'placeholder':'Trusted person"s phone number'}),
        }