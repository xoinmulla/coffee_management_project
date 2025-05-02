from django.urls import path
from .views import coffee_list, coffee_create,edit_coffee, delete_coffee
from . import views


urlpatterns = [
    path('', coffee_list, name='coffee_list'),
    path('create/', coffee_create, name='coffee_create'),  # Add this URL pattern
    path('coffee/<int:pk>/edit/', edit_coffee, name='coffee_edit'),
    path('coffee/<int:pk>/delete/', delete_coffee, name='coffee_delete'),
]