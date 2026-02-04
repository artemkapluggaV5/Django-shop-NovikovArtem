from django.contrib import admin

from django.contrib import admin
from .models import Category, Product

class ProductInline(admin.TabularInline):
    model = Product
    extra = 1
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20
    inlines = [ProductInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_active', 'created_at']
    list_filter = ['is_active', 'category', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20
    list_editable = ['price', 'is_active']
