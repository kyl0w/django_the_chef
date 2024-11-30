# apps/accounts/urls.py

from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),  # Signup page URL
]
