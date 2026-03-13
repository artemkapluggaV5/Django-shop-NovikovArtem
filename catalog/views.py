from decimal import Decimal

from django.contrib.auth.mixins import PermissionRequiredMixin
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
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from cart.forms import CartAddProductForm
from .models import Category, Product
from .forms import CategoryForm, ProductForm


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

@method_decorator(staff_member_required, name='dispatch')
class CategoryCreateView(PermissionRequiredMixin, JsonResponseMixin, CreateView):
    model = Category
    form_class = CategoryForm
    permission_required = 'catalog.add_category'
    raise_exception = True
    template_name = 'catalog/category_form.html'
    success_url = reverse_lazy('categories')

@method_decorator(staff_member_required, name='dispatch')
class CategoryUpdateView(PermissionRequiredMixin, JsonResponseMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    permission_required = 'catalog.change_category'
    template_name = 'catalog/category_form.html'
    success_url = reverse_lazy('categories')

@method_decorator(staff_member_required, name='dispatch')
class CategoryDeleteView(PermissionRequiredMixin, JsonResponseMixin, DeleteView):
    model = Category
    permission_required = 'catalog.delete_category'
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

@method_decorator(staff_member_required, name='dispatch')
class ProductCreateView(PermissionRequiredMixin, JsonResponseMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.add_product'
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('product_list')

@method_decorator(staff_member_required, name='dispatch')
class ProductUpdateView(PermissionRequiredMixin, JsonResponseMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.change_product'
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('product_list')

@method_decorator(staff_member_required, name='dispatch')
class ProductDeleteView(PermissionRequiredMixin, JsonResponseMixin, DeleteView):
    model = Product
    permission_required = 'catalog.delete_product'
    success_url = reverse_lazy('product_list')

@method_decorator(login_required, name='dispatch')
class CategoryDetailView(JsonResponseMixin, DetailView):
    model = Category
    template_name = 'catalog/category_detail.html'
    context_object_name = 'category'


@method_decorator(login_required, name='dispatch')
class ProductDetailView(JsonResponseMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class ProductDetailView(JsonResponseMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context

@permission_required('catalog.change_category', raise_exception=True)
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

@permission_required('catalog.change_product', raise_exception=True)
@require_POST
def update_product_order(request):
    try:
        data = json.loads(request.body)
        order_ids = data.get('order', [])
        for index, prod_id in enumerate(order_ids):
            Product.objects.filter(id=prod_id).update(order=index)
        return JsonResponse({'status': 'ok'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

def permission_denied_view(request, exception=None):
    return render(request, 'catalog/403.html', status=403)