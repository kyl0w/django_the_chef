from django.contrib.auth import views as auth_views
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'), 
    path('logout/', views.logout_view, name='logout'),
]
