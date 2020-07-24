from django.shortcuts import render
from django.views.generic.base import View

from .models import Product

def home(request):
	foods = Product.objects.all()
	return render(request, 'cats/foods.html', {'foods_list': foods})