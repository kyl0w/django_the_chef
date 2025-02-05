from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Dish
from .forms import CategoryForm, DishForm
from accounts.permissions import is_admin, is_manager, is_customer

# List Categories
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

# Create New Category
@is_admin
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

# Update Category
@is_admin
def category_update(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

# Delete Category
@is_admin
def category_delete(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category_confirm_delete.html', {'category': category})

# List Dishes
def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, 'menu/menu.html', {'dishes': dishes})

# Create New Dish
@is_admin
def dish_create(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
    else:
        form = DishForm()
    return render(request, 'dish_form.html', {'form': form})

# Update Dish
@is_admin
def dish_update(request, slug):
    dish = get_object_or_404(Dish, slug=slug)
    if request.method == 'POST':
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
    else:
        form = DishForm(instance=dish)
    return render(request, 'dish_form.html', {'form': form})

# Delete Dish
@is_admin
def dish_delete(request, slug):
    dish = get_object_or_404(Dish, slug=slug)
    if request.method == 'POST':
        dish.delete()
        return redirect('dish_list')
    return render(request, 'dish_confirm_delete.html', {'dish': dish})
