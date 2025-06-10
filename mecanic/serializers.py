from rest_framework import serializers
from .models import Customer, Category, Product, Service


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = 'id', 'name', 'email', 'phone_number'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id', 'name', 'description'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id', 'name', 'quantity', 'price', 'description', 'category'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = 'id', 'name', 'description', 'price', 'delivery_time', 'category'