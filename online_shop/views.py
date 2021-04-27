from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from itertools import chain
from .models import Category, Product, OnlineShopUser, Cart, Wishlist

# Create your views here.

# Checking wether user is logged in.
def is_logged_in(request):
	try:
		if request.session['userid']:
			return True
	except KeyError:
		return False


# Returning dict with userid and name if user is logged in.
def logged_in_info(request):
	try:
		if request.session['userid']:
			return {
				'userid': request.session['userid'],
				'uname': request.session['user_name']
			}
	except KeyError:
		return {}


def index(request):
	data = logged_in_info(request)
	data['categories'] = Category.objects.all().order_by('name')
	return render(request, 'index.html', data)
	

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
	
	data = logged_in_info(request)
	data['products'] = products
	return render(request, 'products.html', data)


# Retrieving products based on category selected.
def category(request, category_id):
	products = Product.objects.filter(category_id=category_id).order_by('name')
	for product in products:
		product.final_price = product.price - ((product.discount * product.price) / 100)
	
	data = logged_in_info(request)
	data['products'] = products
	return render(request, 'products.html', data)


# Retrieving product info
def product(request, product_id):
	data = logged_in_info(request)
	try:
		product = Product.objects.get(pk=product_id)
		product.discount_amt = (product.discount * product.price) / 100
		product.final_price = product.price - product.discount_amt
		data['product'] = product
	except:
		pass
	else:
		if is_logged_in(request):
			product.cart = Cart.objects.filter(product_id=product.id, user_id=request.session['userid']).exists()
			product.wishlist = Wishlist.objects.filter(product_id=product.id, user_id=request.session['userid']).exists()

	return render(request, 'product.html', data)


# Adding product to the cart.
def add_to_cart(request, product_id):
	try:
		product = Product.objects.get(pk=product_id)
		user = OnlineShopUser.objects.get(pk=request.session['userid'])
		if not Cart.objects.filter(product_id=product.id, user_id=request.session['userid']).exists():
			cart_obj = Cart(product_id=product, user_id=user)
			cart_obj.save()
	except:
		pass
	return redirect("/product/{0}".format(product_id))


# Adding product to the wishlist.
def add_to_wishlist(request, product_id):
	try:
		product = Product.objects.get(pk=product_id)
		user = OnlineShopUser.objects.get(pk=request.session['userid'])
		if not Wishlist.objects.filter(product_id=product.id, user_id=request.session['userid']).exists():
			wishlist_obj = Wishlist(product_id=product, user_id=user)
			wishlist_obj.save()
	except:
		pass
	return redirect("/product/{0}".format(product_id))


# Verifying the existence of user and verifying password. 
def verify_user(request):
	if request.method == 'POST':
		email = request.POST['email']
		pwd = request.POST['pwd']

		try:
			user = OnlineShopUser.objects.get(email=email)
			if check_password(pwd, user.password):
				request.session['userid'] = user.id
				request.session['user_name'] = user.name
				return HttpResponse("1")
			else:
				return HttpResponse("You have entered incorrect password.")
		except:
			return HttpResponse("User with email {0} doesn't exist.".format(email))


# Validating non-existence of user with email or mobile no given during registration. 
def validate_user(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		mob = request.POST['mob']
		pwd = request.POST['pwd']
		
		if OnlineShopUser.objects.filter(email=email).exists():
			return HttpResponse("User with email {0} already exists.".format(email))

		elif OnlineShopUser.objects.filter(mobile=mob).exists():
			return HttpResponse("User with mobile no {0} already exists.".format(mob))

		else:
			user = OnlineShopUser(name=name, email=email, mobile=mob, password=make_password(pwd))
			user.save()
			request.session['userid'] = user.id
			request.session['user_name'] = user.name
			return HttpResponse("1")


# Signout
def signout(request):
	try:
		del request.session['userid']
		del request.session['user_name']
	except KeyError:
		pass
	return redirect("/")
