from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views_api

app_name = 'mecanic'
mecanic_api_router = SimpleRouter()
mecanic_api_router.register('api/customers', views_api.CustomerViewSet, basename='customer')
mecanic_api_router.register('api/categories', views_api.CategoryViewSet, basename='category')
mecanic_api_router.register('api/products', views_api.ProductViewSet, basename='product')
mecanic_api_router.register('api/services', views_api.ServiceViewSet, basename='service')
urlpatterns = [
    path('', include(mecanic_api_router.urls)),
]
