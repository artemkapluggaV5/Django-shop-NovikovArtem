from decimal import Decimal
from django.db import models
from django.db.models import Q
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.forms.models import model_to_dict
from django.views.generic import RedirectView, ListView, CreateView, UpdateView, DeleteView, DetailView
import json

from cart.forms import CartAddProductForm
from .models import Category, Product
from .forms import CategoryForm, ProductForm, EmployeeCreationForm


class JsonResponseMixin:

    def render_to_response(self, context, **response_kwargs):
        fmt = self.request.GET.get('format', '').strip('/').lower()
        if fmt == 'json' or self.request.headers.get('Accept') == 'application/json':
            return self.render_to_json_response(context)
        return super().render_to_response(context, **response_kwargs)

    def render_to_json_response(self, context):
        def serialize_item(obj):
            data = {}
            for field in obj._meta.fields:
                name = field.name
                value = getattr(obj, name)

                if isinstance(field, (models.FileField, models.ImageField)):
                    if value and value.name:
                        try:
                            data[name] = value.url
                        except ValueError:
                            data[name] = None
                    else:
                        data[name] = None

                elif isinstance(value, Decimal):
                    data[name] = float(value)

                else:
                    data[name] = value
            return data

        if 'object_list' in context:
            data = [serialize_item(obj) for obj in context['object_list']]
        elif 'object' in context:
            data = serialize_item(context['object'])
        else:
            data = context

        return JsonResponse(data, safe=False)


class HomeRedirectView(RedirectView):
    pattern_name = 'categories'


class CategoryListView(JsonResponseMixin, ListView):
    model = Category
    template_name = 'catalog/catalog_list.html'
    context_object_name = 'categories'
    ordering = ['order']
    paginate_by = 12

    def get_queryset(self):
        queryset = Category.objects.all().order_by('order')
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(name__icontains=q)
        return queryset
class CategoryCreateView(JsonResponseMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_form.html'
    success_url = reverse_lazy('categories')


class CategoryUpdateView(JsonResponseMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_form.html'
    success_url = reverse_lazy('categories')


class CategoryDeleteView(JsonResponseMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('categories')


class ProductListView(JsonResponseMixin, ListView):
    model = Product
    queryset = Product.objects.select_related('category')
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 20

    def get_queryset(self):
        queryset = Product.objects.select_related('category').all().order_by('order')
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(name__icontains=q)
        return queryset


class ProductCreateView(JsonResponseMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('product_list')


class ProductUpdateView(JsonResponseMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('product_list')


class ProductDeleteView(JsonResponseMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')


class CategoryDetailView(JsonResponseMixin, DetailView):
    model = Category
    template_name = 'catalog/category_detail.html'  # создай этот файл
    context_object_name = 'category'


class ProductDetailView(JsonResponseMixin, DetailView):
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

class ProductDetailView(JsonResponseMixin, DetailView):
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