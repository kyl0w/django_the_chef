from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Define the menu view
@login_required
def menu(request):
    return render(request, 'menu/menu.html')
