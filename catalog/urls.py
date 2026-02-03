from django.urls import path
from catalog import views


urlpatterns = [
    path('', views.HomeRedirectView.as_view(), name='home'),

    # Категории
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('categories/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category-detail'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),

    # Товары
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/create/', views.ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),
]
