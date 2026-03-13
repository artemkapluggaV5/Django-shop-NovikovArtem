from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

User = get_user_model()

class EmployeeCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (User.USERNAME_FIELD, "first_name", "last_name")
        error_messages = {
            User.USERNAME_FIELD: {
                'unique': "Эта почта уже занята. Попробуйте другую почту.",
            },
        }

class EmployeeLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control border-0 shadow-none py-2',
        'placeholder': 'Электронная почта',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control border-0 shadow-none py-2',
        'placeholder': 'Пароль',
    }))