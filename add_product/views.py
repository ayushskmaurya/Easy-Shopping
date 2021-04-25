from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from PIL import Image
from online_shop.models import Category, Product

# Create your views here.

def login(request):
	if request.method == 'POST':
		uname = request.POST['uname']
		pwd = request.POST['pwd']

		user = authenticate(username=uname, password=pwd)
		if user is not None:
			request.session['username'] = uname
		else:
			request.session['error_message'] = "Please enter correct username and password."
			request.session['type_of_error'] = "login"

	data = {}
	try:
		if request.session['username']:
			data['is_logged_in'] = True
			data['categories'] = Category.objects.all()
	except KeyError:
		data['is_logged_in'] = False
	try:
		if request.session['error_message']:
			data['error_message'] = request.session['error_message']
			data['type_of_error'] = request.session['type_of_error']
			del request.session['error_message']
			del request.session['type_of_error']
	except KeyError:
		pass
	try:
		if request.session['success_message']:
			data['success_message'] = request.session['success_message']
			data['type_of_success'] = request.session['type_of_success']
			del request.session['success_message']
			del request.session['type_of_success']
	except KeyError:
		pass

	return render(request, 'add_product.html', data)


def logout(request):
	try:
		del request.session['username']
	except KeyError:
		pass
	return redirect("/add_product")


def add_product(request):
	if request.method == 'POST':
		product_name = request.POST['product-name'].strip()
		category_id = request.POST['category']
		discount = request.POST['discount'].strip()
		desc = request.POST['desc'].strip()

		if len(product_name) == 0 or category_id == "":
			request.session['error_message'] = "Please enter all the required fields correctly."
			request.session['type_of_error'] = "product"
		else:
			try:
				price = int(request.POST['price'].strip())
				if len(discount) == 0:
					discount = 0
				else:
					discount = int(discount)
				img = Image.open(request.FILES['product-img'])
			except:
				request.session['error_message'] = "Please enter all the required fields correctly."
				request.session['type_of_error'] = "product"

		try:
			if request.session['error_message']:
				pass
		except KeyError:
			category = Category.objects.get(pk=category_id)
			product = Product(name=product_name, category_id=category, price=price)
			if discount != 0:
				product.discount = discount
			if len(desc) != 0:
				product.desc = desc
			product.save()
			img.save("static\\products_images\\{0}.jpg".format(product.id))
			request.session['success_message'] = "Product {0} added successfully.".format(product.name)
			request.session['type_of_success'] = "product"

	return redirect("/add_product")


def add_category(request):
	if request.method == 'POST':
		category_name = request.POST['category-name'].strip()

		if len(category_name) == 0:
			request.session['error_message'] = "Please enter all the required fields correctly."
			request.session['type_of_error'] = "category"
		else:
			try:
				img = Image.open(request.FILES['category-img'])
			except:
				request.session['error_message'] = "Please enter all the required fields correctly."
				request.session['type_of_error'] = "category"

		try:
			if request.session['error_message']:
				pass
		except KeyError:
			category = Category(name=category_name)
			category.save()
			img.save("static\\categories_images\\{0}.jpg".format(category.id))
			request.session['success_message'] = "Category {0} added successfully.".format(category.name)
			request.session['type_of_success'] = "category"

	return redirect("/add_product")
