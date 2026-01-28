from django.urls import path

from catalog import views
urlpatterns = [
    path('', views.home_redirect, name='home'),

    path('categories/', views.categories, name='categories'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
]