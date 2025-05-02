from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['coffee', 'quantity', 'delivery_address']  # Ensure 'coffee' is included

from django import forms
from django.utils import timezone
from .models import Order
from coffee.models import Coffee  # Assuming the Coffee model is in the coffee app

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['coffee', 'quantity', 'delivery_address', 'status', 'order_date']  # Include all fields except 'customer' as the customer is logged in

    def __init__(self, *args, **kwargs):
        # If you have the customer (logged in user) available, set it automatically
        super(OrderForm, self).__init__(*args, **kwargs)
        if 'customer' not in self.initial:
            self.initial['customer'] = kwargs.get('initial', {}).get('customer', None)

        # Optional: Add a custom validation for order_date if needed
        self.fields['order_date'].initial = timezone.now()

    def clean(self):
        cleaned_data = super().clean()

        # Additional validation logic if needed
        quantity = cleaned_data.get('quantity')
        if quantity and quantity <= 0:
            raise forms.ValidationError("Quantity must be a positive integer.")

        return cleaned_data
