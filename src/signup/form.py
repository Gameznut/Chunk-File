import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password

# from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Individual

class RegisterForm(forms.ModelForm):
    error_messages = {
        "password_mismatch": ("The two password fields didn’t match."),
        "no_symbol": ("No @ in thepassword field")
    }
    email = forms.EmailField(
        max_length=100,
        required = True,
        help_text='Enter Email Address',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )
    first_name = forms.CharField(
    max_length=100,
    required = True,
    help_text='Enter First Name',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
    )
    last_name = forms.CharField(empty_value="testing",
    max_length=100,
    required = True,
    help_text='Enter Last Name',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'},),
    )
    username = forms.CharField(
    max_length=200,
    required = True,
    help_text='Enter Username',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    )
    password = forms.CharField(
    help_text='Enter Password',
    required = True,
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    password1 = forms.CharField(
    required = True,
    help_text='Enter Password Again',
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
    )
    
    

    class Meta:
        model = Individual
        fields = [
        'username', 'email', 'first_name', 'last_name', 'password1',"password"
        ]

    
    def clean_password(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        
        if password and password1 and password != password1:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )  
        if not "@" in password1 and not "@" in password:
            raise ValidationError(
                self.error_messages["no_symbol"],
                code="no_symbol",
            )       
        return password


class LoginForm(forms.ModelForm):
    # error_messages = {
    #     "password_mismatch": ("The two password fields didn’t match."),
    #     "no_symbol": ("No @ in thepassword field")
    # }
    email = forms.EmailField(
        max_length=100,
        required = True,
        help_text='Enter Email Address',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )
    username = forms.CharField(
        max_length=200,
        required = True,
        help_text='Enter Username',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    )
    password = forms.CharField(
        help_text='Enter Password',
        required = True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
  

    class Meta:
        model = Individual
        fields = [
        'username', 'password'
        ]

    
    # def clean_password(self):
    #     password = self.cleaned_data.get("password")
        
    #     if password:
    #         raise ValidationError(
    #             self.error_messages["password_mismatch"],
    #             code="password_mismatch",
    #         )  
      
    #     return password



