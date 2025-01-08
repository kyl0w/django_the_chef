# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login_view'),
    path('login/auth/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
