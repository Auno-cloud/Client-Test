from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from .models import Customer, Category, Product, Service



class CustomerTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.customer = Customer.objects.create(
            name='Test Customer',
            email='testcustomer@example.com',
            phone_number='1234567890'
        )
        

    def test_get_list_customers(self):
        url = reverse('mecanic:customer-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_customer_detail(self):
        url = reverse('mecanic:customer-detail', args=[self.customer.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Customer.objects.get().name, 'Test Customer')

    def test_create_customer(self):
        url = reverse('mecanic:customer-list')
        data = {
            'name': 'Customer Test',
            'email': 'testcustomer2@example.com',
            'phone_number': '123456789'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.get(id=2).name, 'Customer Test')
    
    def test_update_customer(self):
        url = reverse('mecanic:customer-detail', args=[self.customer.pk])
        data = {'name': 'Name Different',
                'email': 'newemail@email.com',
                'phone_number': '987654321'}
        response = self.client.put(url,data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Customer.objects.get().name, 'Name Different')
    
    def test_delete_customer(self):
        url = reverse('mecanic:customer-detail', args=[self.customer.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



# Test cases for Category model
class CategoryTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(
            name='Category Test',
            description='Description of the category'
        )

    def test_get_list_categories(self):
        url = reverse('mecanic:category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_category_detail(self):
        url = reverse('mecanic:category-detail', args=[self.category.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_category(self):
        url = reverse('mecanic:category-list')
        data = {
            'name': 'New Category',
            'description': 'Description of the new category'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.get(id=2).name, 'New Category')

    def test_update_category(self):
        url = reverse('mecanic:category-detail', args=[self.category.pk])
        data = {'name': 'Category Updated',
                'description': 'Updated description'}
        response = self.client.put(url,data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.get().name, 'Category Updated')

    def test_delete_category(self):
        url = reverse('mecanic:category-detail', args=[self.category.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ProductTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(
            name='Product Test',
            quantity=10,
            price=100.00,
            description='Description of the product',
            category= Category.objects.create(name='Category for product test')

        )
    
    def test_get_list_products(self):
        url= reverse('mecanic:product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_product_detail(self):
        url = reverse('mecanic:product-detail', args=[self.product.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.get().name, 'Product Test')

    def test_create_product(self):
        url = reverse('mecanic:product-list')
        data = {
            'name': 'New Product',
            'quantity': 5,
            'price': 50.00,
            'description': 'Description of the new product',
            'category': self.product.category.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.get(id=2).name, 'New Product')

    def test_update_product(self):
        url =reverse('mecanic:product-detail', args=[self.product.pk])
        data = {'name': 'Product Updated',
                'quantity': 20,
                'price': 200.00,
                'description': 'Updated description',
                'category': self.product.category.id
                }
        response = self.client.put(url,data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.get().name, 'Product Updated')
    
    def test_delete_product(self):
        url = reverse('mecanic:product-detail', args = [self.product.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ServiceTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.service = Service.objects.create(
            name= 'Service Test',
            description = 'Description of the service',
            price = 50.00,
            delivery_time= 3,
            delivery_time_unit = 'horas'
        )

    def test_get_list_services(self):
        url = reverse('mecanic:service-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_service_detail(self):
        url = reverse('mecanic:service-detail', args=[self.service.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Service.objects.get().name, 'Service Test')

    def test_create_service(self):
        url = reverse('mecanic:service-list')
        data = {
            'name': 'New service test',
            'description': 'New description service',
            'price': 10.00,
            'delivery_time': 9,
            'delivery_time_unit': 'Minutos'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Service.objects.get(id=2).name, 'New service test')

    def test_update_service(self):
        url = reverse('mecanic:service-detail', args=[self.service.pk])
        data = {
            'name': 'Service Update',
            'description': 'Description for updated service',
            'price': 100.00,
            'delivery_time': 2,
            'delivery_time_unit': 'horas'
        }        
        response = self.client.put(url,data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Service.objects.get().name, 'Service Update')
    
    def test_delete_service(self):
        url = reverse('mecanic:service-detail', args=[self.service.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
