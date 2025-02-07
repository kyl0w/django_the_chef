from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import RegisterForm

def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'accounts/login.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  

            if user.role == 'Manager':
                return redirect('manager')  
            elif user.role == 'Employee':
                return redirect('worker')   
            
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
    else:
        form = AuthenticationForm()

    return render(request, 'home.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            auth_login(request, user)
            if user.role == 'Manager':
                return redirect('manager')
            elif user.role == 'Employee':
                return redirect('worker')
            else:
                return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/signup.html', {'form': form})

def logout_view(request):
    auth_logout(request) 
    return redirect('login')  
