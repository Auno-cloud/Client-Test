from django.db import models
from django.conf import settings

# Create your models here.



class Category(models.Model):
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    name = models.CharField(max_length=50, verbose_name="Nome", unique=True)
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")


    def __str__(self):
        return self.name

class Customer(models.Model):
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    name = models.CharField(max_length=50, verbose_name="Nome")
    email = models.EmailField(unique=True, verbose_name="Email")
    phone_number = models.CharField(max_length=15, verbose_name="Telefone", unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    def __str__(self):
        return self.name

class Product(models.Model):
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
    name = models.CharField(max_length=50, verbose_name="Nome")
    quantity = models.IntegerField(verbose_name="Quantidade")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Categoria")

    def __str__(self):
        return self.name

class Service(models.Model):

    delivery_time_choices = [('min', 'Minutos'), ('h', 'Horas'), ('d', 'Dias')]
    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"
    name = models.CharField(max_length=50, verbose_name="Nome", unique=True)
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    delivery_time = models.IntegerField(verbose_name="Tempo de Entrega", blank=True, null=True)
    delivery_time_unit = models.CharField(max_length=10, choices=delivery_time_choices, blank=True, default='hj', verbose_name="Unidade de Tempo", help_text="Tempo de entrega " \
    " em Minutos, Horas ou Dias")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Categoria")

    def __str__(self):
        return self.name