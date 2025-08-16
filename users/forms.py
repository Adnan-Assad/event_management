from django import forms
from users.models import CustomUser
from django.contrib.auth.forms import (
    UserCreationForm, UserChangeForm, 
    PasswordChangeForm, AuthenticationForm, 
    PasswordResetForm, SetPasswordForm
)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))

    class Meta:
        model = CustomUser
        fields = [
            'username', 'first_name', 'last_name',
            'email', 'phone_number', 'profile_picture',
            'password1', 'password2'
        ]

 
class EditProfileForm(UserChangeForm):
    password = None    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number' ]


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))


 
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))


class CustomPasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))

    
class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))

    class Meta:
        model = CustomUser
        fields = [
            'username', 'first_name', 'last_name',
            'email', 'phone_number', 'profile_picture',
            'password1', 'password2'
        ]