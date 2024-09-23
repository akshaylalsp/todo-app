from .models import CustomUser,Tasks
from django.forms import ModelForm,Form
from django.contrib.auth.forms import UserCreationForm
from django import forms
class CustomUserRegistrationForm(UserCreationForm):
    
    
    class Meta:
        model = CustomUser
        fields = ['username','phone']


class TaskCreateForm(ModelForm):

    class Meta:
        model = Tasks
        fields = ['name','description']

class LoginForm(Form):
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)