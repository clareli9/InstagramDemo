## Custom User Creation Form
from django import forms 
from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm
from Insta.models import InstaUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # Some override
        model = InstaUser
        fields = ('username', 'email', 'profile_pic',)
