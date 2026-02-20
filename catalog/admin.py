from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Product


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1
    prepopulated_fields = {'slug': ('name',)}
    fields = ['name', 'slug', 'price', 'is_active']


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
    list_display = ['get_html_image', 'name', 'category', 'price', 'is_active', 'created_at']
    list_filter = ['is_active', 'category', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20
    list_editable = ['price', 'is_active']

    def get_html_image(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50 style='border-radius: 5px;'>")
        return "Нет фото"

    get_html_image.short_description = "Миниатюра"