from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth import logout

def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'accounts/login.html')

def login_view(request):
    # Check if the request method is POST
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after successful registration
            return redirect('home')  # Redirect to home or another page
        else:
            # If the form is not valid, render the form with error messages
            return render(request, 'accounts/signup.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'accounts/signup.html', {'form': form})
def logout_view(request):
    logout(request)
    return render(request, 'accounts/login.html')
