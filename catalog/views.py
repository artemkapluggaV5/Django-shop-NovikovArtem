from django.shortcuts import render, get_object_or_404, redirect
from .models import Category
from .forms import CategoryForm


def home_redirect(request):
    return redirect('categories')


def categories(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()

    return render(request, 'catalog/catalog_list.html', {
        'categories': categories,
        'form': form
    })


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        if 'delete' in request.POST:
            category.delete()
            return redirect('categories')

        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'catalog/category_form.html', {
        'form': form,
        'category': category
    })
