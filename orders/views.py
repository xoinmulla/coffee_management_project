from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order  # Ensure the Order model exists
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

def orders_list(request):
    orders = Order.objects.all()  # Fetch all orders from the database
    return render(request, 'orders/orders_list.html', {'orders': orders})

# views.py
@login_required
def order_coffee(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Set the logged-in user as the customer before saving
            order = form.save(commit=False)
            order.customer = request.user
            order.save()
            return redirect('order_success')  # Redirect to a success page after saving
    else:
        form = OrderForm()

    return render(request, 'orders/order_form.html', {'form': form})

def order_form(request):
    # Logic for handling the order form
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Process the order (saving to the database, etc.)
            form.save()
            return redirect('orders_list')  # Redirect to orders list or another page
    else:
        form = OrderForm()

    return render(request, 'orders/orders_form.html', {'form': form})

def generate_bill(request, order_id):
    # Fetch the specific order by ID
    order = get_object_or_404(Order, id=order_id)
    
    # Calculate the total price
    total_price = order.total_price()

    # Render the bill page
    return render(request, 'orders/bill.html', {'order': order, 'total_price': total_price})