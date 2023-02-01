from django import forms

from .models import UserLog
from django.contrib.auth.models import User

class ImageForm(forms.ModelForm):
   class Meta:
       model = UserLog
       fields = ['image']        
             
       
       
