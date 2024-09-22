from .models import CustomUser,Tasks
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class CustomUserRegistrationForm(UserCreationForm):
    
    
    class Meta:
        model = CustomUser
        fields = ['username','phone']