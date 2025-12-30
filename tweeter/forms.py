from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model=Tweet
        fields=['text','photo'] # Dealing with the our user Form,Use the list

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2') # Whenver Dealing with the Admin site forms we should use the tuple