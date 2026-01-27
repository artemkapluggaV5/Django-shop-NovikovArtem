from django.urls import path

from catalog import views
urlpatterns = [
    path('categories/', views.categories_list, name='categories_list'),
    path('categories/', views.category_create, name='category_create'),
    path('categories/<int:pk>/', views.category_edit, name='category_edit'),
    path('categories/<int:pk>/', views.category_delete, name='category_delete'),
    path('', views.home_redirect, name='home'),

]