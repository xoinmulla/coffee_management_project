from django.shortcuts import render, get_object_or_404, redirect
from .models import Coffee
from .forms import CoffeeForm

def coffee_list(request):
    coffees = Coffee.objects.all()
    return render(request, 'coffee/coffee_list.html', {'coffees': coffees})

def coffee_create(request):
    if request.method == 'POST':
        form = CoffeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('coffee_list')
    else:
        form = CoffeeForm()
    return render(request, 'coffee/coffee_form.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Coffee
from .forms import CoffeeForm  # You need to create this form
from django.contrib.auth.decorators import login_required

@login_required
def edit_coffee(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    if request.method == 'POST':
        form = CoffeeForm(request.POST, request.FILES, instance=coffee)
        if form.is_valid():
            form.save()
            return redirect('coffee_list')
    else:
        form = CoffeeForm(instance=coffee)
    return render(request, 'coffee/edit_coffee.html', {'form': form})

@login_required
def delete_coffee(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    if request.method == 'POST':
        coffee.delete()
        return redirect('coffee_list')
    return render(request, 'coffee/confirm_delete.html', {'coffee': coffee})
