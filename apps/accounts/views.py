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
            auth_login(request, user)  # Using `auth_login` to avoid conflict

            next_url = request.GET.get('next', 'home')  # Redirect to the next URL or home
            return redirect(next_url)
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # This will automatically save the user and return the user object
            # Set the password from the form before login
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            auth_login(request, user)  # Log the user in
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def logout_view(request):
    auth_logout(request)  # Log out the user
    return redirect('login')  # Redirect to the login page after logout
