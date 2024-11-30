from django.shortcuts import render

# Define the menu view
def menu(request):
    return render(request, 'menu/menu.html')
