from django.contrib import admin

# admin.py
from django.contrib import admin
from .models import PizzaPie, MenuItem, Order, OrderItem

@admin.register(PizzaPie)
class PizzaPieAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    # Add other configurations as needed

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price')
    list_filter = ('restaurant',)
    # Add other configurations as needed

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'customer_name', 'customer_address', 'order_time', 'is_delivered')
    list_filter = ('restaurant', 'is_delivered')
    # Add other configurations as needed

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'item', 'quantity')
    

