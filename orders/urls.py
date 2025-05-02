from django.urls import path

from coffee import views
from .views import generate_bill, order_coffee, orders_list, order_form  # Ensure both functions exist in views.py

urlpatterns = [
    
    path('list/', orders_list, name='orders_list'),
    path('order/', order_coffee, name='order_coffee'),
    path('form/', order_form, name='order_form'),  # Ensure this line is added
    path('order/<int:order_id>/bill/', generate_bill, name='generate_bill'),  # Bill generation path
     
]