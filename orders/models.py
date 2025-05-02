from django.db import models
from django.conf import settings
from django.utils import timezone  # Import timezone for default value
from coffee.models import Coffee  # Assuming you have the Coffee model

# Define status choices
STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Completed', 'Completed'),
    ('Cancelled', 'Cancelled'),
]

class Order(models.Model):
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    delivery_address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)  # Temporarily allow null
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True)
    order_date = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return f"Order of {self.quantity} {self.coffee.name} for {self.customer}"
    
    def total_price(self):
        # Calculate total price based on coffee price and quantity
        return self.coffee.price * self.quantity

