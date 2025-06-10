from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CustomerSerializer, CategorySerializer, ProductSerializer, ServiceSerializer
from .models import Customer, Category, Product, Service
from rest_framework.pagination import PageNumberPagination


# Create your views here.

class Pagination(PageNumberPagination):
    page_size = 10

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all().order_by('id')
    serializer_class = CustomerSerializer
    pagination_class = Pagination

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

