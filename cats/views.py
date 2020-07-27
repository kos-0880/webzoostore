from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Product

class ProductsView(ListView):
	# Список продуктов
	model = Product
	queryset = Product.objects.filter(draft=False)

class ProductDetailView(DetailView):
	# полное описание
	model = Product
	slug_field = 'url'

