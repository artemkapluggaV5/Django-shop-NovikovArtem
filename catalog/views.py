from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import redirect

from django.shortcuts import get_object_or_404
from .models import Category, Product
from .models import Category
from .forms import CategoryForm
from .models import Category

def home(request):
    categories = Category.objects.all()
    return render(request, "catalog/catalog_list.html", {
        'title': 'Каталог',
        'categories': categories
    })


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'catalog/catalog_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories_list')
    else:
        form = CategoryForm()
    return render(request, 'catalog/category_form.html', {'form': form})

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'catalog/category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('categories_list')
    return render(request, 'catalog/category_confirm_delete.html', {'category': category})

def home_redirect(request):
    return redirect('categories_list')