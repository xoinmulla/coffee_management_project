from django.contrib import admin
from .models import Coffee

@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image')
    search_fields = ('name', 'description')
    list_filter = ('price',)
