from django.contrib import admin
from .models import Coffee, Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'coffee', 'quantity', 'status', 'order_date')  # Make sure these fields exist
    ordering = ('order_date',)  # Ordering by 'order_date' assuming it's a valid field
    list_filter = ('status', 'order_date')  # Ensure these are valid fields

admin.site.register(Order, OrderAdmin)

