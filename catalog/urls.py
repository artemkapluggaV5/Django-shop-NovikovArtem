from django.urls import path, include
from catalog import views
from django.contrib.auth import views as auth_views
from django.conf import settings
import users.views as user_views
from catalog.views import HomeView
from users.forms import EmployeeLoginForm

urlpatterns = [
    path('', views.HomeRedirectView.as_view(), name='home'),

    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('categories/add/', views.CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/add/', views.ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('categories/update-order/', views.update_category_order, name='update_category_order'),
    path('login/',
         auth_views.LoginView.as_view(template_name='catalog/login.html', authentication_form=EmployeeLoginForm),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', user_views.register_view, name='register'),
    path('update-product-order/', views.update_product_order, name='update_product_order'),
    path('test/', HomeView.as_view(), name='home'),
    path('frontend/categories/<int:pk>/', views.FrontCategoryDetailView.as_view(), name='frontend-category-detail'),
    path('frontend/products/<int:pk>/', views.FrontProductDetailView.as_view(), name='frontend-product-detail'),
    path('catalog/<int:pk>/', views.SingleCategoryView.as_view(), name='single-category'),
]
