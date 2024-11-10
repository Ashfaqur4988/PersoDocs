from django import forms
from .models import Doc
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class DocForm(forms.ModelForm):
    class Meta:
        model = Doc
        fields = ['title', 'file']
        
    
class UploadExcelForm(forms.Form):
    excel_file = forms.FileField()
    

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')