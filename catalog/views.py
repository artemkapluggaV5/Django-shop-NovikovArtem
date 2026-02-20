from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import RedirectView, ListView, CreateView, UpdateView, DeleteView, DetailView
import json

from cart.forms import CartAddProductForm
from .models import Category, Product
from .forms import CategoryForm, ProductForm, EmployeeCreationForm


class HomeRedirectView(RedirectView):
    pattern_name = 'categories'


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/catalog_list.html'
    context_object_name = 'categories'
    ordering = ['order']

    def get_queryset(self):
        queryset = super().get_queryset().order_by('order')
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(name__icontains=q)
        return queryset

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_form.html'
    success_url = reverse_lazy('categories')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_form.html'
    success_url = reverse_lazy('categories')


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('categories')


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.select_related('category')
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'catalog/category_detail.html'  # создай этот файл
    context_object_name = 'category'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'  # и этот
    context_object_name = 'product'

def register_view(request):
    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = EmployeeCreationForm()
    return render(request, 'catalog/register.html', {'form': form})

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context


@require_POST
def update_category_order(request):
    try:
        data = json.loads(request.body)
        order_ids = data.get('order', [])

        for index, cat_id in enumerate(order_ids):
            Category.objects.filter(id=cat_id).update(order=index)

        return JsonResponse({'status': 'ok'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@require_POST
def update_product_order(request):
    try:
        data = json.loads(request.body)
        order_ids = data.get('order', [])
        for index, prod_id in enumerate(order_ids):
            Product.objects.filter(id=prod_id).update(order=index) # Убедитесь, что у Product есть поле order
        return JsonResponse({'status': 'ok'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)