from django.urls import path
from catalog import views


urlpatterns = [
    path('', views.home_redirect, name='home'),

    # Категории
    path('categories/', views.categories, name='categories'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),

    # Товары (пока можно закомментировать, если ломает)
    # path('products/', views.product_list, name='product_list'),
    # path('products/<int:pk>/', views.product_detail, name='product_detail'),
]
