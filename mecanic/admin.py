from django.contrib import admin
from .models import Category, Customer, Product, Service



admin.site.register(Category)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = 'id','name', 'email', 'phone_number', 'created_at', 'updated_at',
    search_fields = 'name', 'email',
    list_filter = 'name', 
    list_display_links = 'name', 'email',
    list_per_page = 10

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'id','name', 'quantity', 'price', 'category',
    search_fields = 'name', 'category__name',
    list_filter = 'category', 'price', 'name', 'quantity'
    list_display_links = 'name', 'quantity',

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = 'id','name', 'price', 'delivery_time', 'delivery_time_unit', 'category',
    search_fields = 'name', 'category__name',
    list_filter = 'category', 'price', 'delivery_time', 'name', 'delivery_time_unit'
    list_display_links = 'name', 'price',


