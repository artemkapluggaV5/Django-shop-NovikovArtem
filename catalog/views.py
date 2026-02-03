
from django.urls import reverse_lazy
from django.views.generic import RedirectView, ListView, CreateView, UpdateView, DeleteView
from .models import Category, Product
from .forms import CategoryForm, ProductForm

class HomeRedirectView(RedirectView):
    pattern_name = 'categories'

class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/catalog_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(name__icontains=q)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CategoryForm()  # Форма для быстрого добавления
        return context

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_form.html'
    success_url = reverse_lazy('categories')

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('categories')


# 3. ТОВАРЫ
class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductForm()
        return context

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