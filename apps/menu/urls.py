from django.urls import path
from . import views

urlpatterns = [
    # URLs para Categorias
    path('categories/', views.category_list, name='category_list'),
    path('categories/new/', views.category_create, name='category_create'),
    path('categories/<slug:slug>/edit/', views.category_update, name='category_update'),
    path('categories/<slug:slug>/delete/', views.category_delete, name='category_delete'),

    # URLs para Pratos
    path('dishes/', views.dish_list, name='menu'),
    path('dishes/new/', views.dish_create, name='dish_create'),
    path('dishes/<slug:slug>/edit/', views.dish_update, name='dish_update'),
    path('dishes/<slug:slug>/delete/', views.dish_delete, name='dish_delete'),
]
