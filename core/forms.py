from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser, Student

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['course', 'session_start', 'session_end']
