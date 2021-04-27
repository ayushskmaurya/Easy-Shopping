from django.shortcuts import render
from itertools import chain
from .models import Category, Product

# Create your views here.

def index(request):
	categories = Category.objects.all().order_by('name')
	return render(request, 'index.html', {'categories': categories})
	

# Retrieving products based on searched query.
def searched(request, query):
	# Retrieving products by searching for specified pattern(query) in column 'name' from 'product' table.
	products1 = Product.objects.filter(name__icontains=query).order_by('name')
	products1_id = [product.id for product in products1]

	# Retrieving products by searching for specified pattern(query) in column 'name' from 'category' table.
	categories = Category.objects.filter(name__icontains=query).order_by('name')
	categories_id = [category.id for category in categories]
	products2 = Product.objects.filter(category_id__in=categories_id).exclude(id__in=products1_id).order_by('name')
	
	products = list(chain(products1, products2))

	for product in products:
		product.final_price = product.price - ((product.discount * product.price) / 100)
	return render(request, 'products.html', {'products': products})


# Retrieving products based on category selected.
def category(request, category_id):
	products = Product.objects.filter(category_id=category_id).order_by('name')
	for product in products:
		product.final_price = product.price - ((product.discount * product.price) / 100)
	return render(request, 'products.html', {'products': products})


# Retrieving product info
def product(request, product_id):
	data = {}
	try:
		product = Product.objects.get(pk=product_id)
		product.discount_amt = (product.discount * product.price) / 100
		product.final_price = product.price - product.discount_amt
		data['product'] = product
	except:
		pass
	return render(request, 'product.html', data)
