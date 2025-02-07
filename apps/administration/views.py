from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import user_passes_test

from .forms import AdminSignupForm, AdminLoginForm
from accounts.permissions import is_admin, is_manager

def admin_signup(request):
    if request.method == 'POST':
        form = AdminSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()
            messages.success(request, "Cadastro realizado com sucesso. Faça login para continuar.")
            return redirect('admin_login')
    else:
        form = AdminSignupForm()
    return render(request, 'administration/signup.html', {'form': form})

def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('admin_dashboard')
    else:
        form = AdminLoginForm()
    return render(request, 'administration/login.html', {'form': form})

def admin_logout(request):
    auth_logout(request)
    return redirect('admin_login')

@user_passes_test(is_admin, login_url='home')
def admin_dashboard(request):
    return render(request, 'administration/dashboard.html')