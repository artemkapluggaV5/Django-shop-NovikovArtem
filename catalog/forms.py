from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Category
from django import forms
from .models import Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'description', 'is_active', 'image']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите название"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'slug', 'description', 'price', 'is_active', 'image']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите название"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

User = get_user_model()

class EmployeeCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (User.USERNAME_FIELD,)
