# Easy-Shopping
Django based E-commerce Website

* Easy Shopping is reliable and easy-to-use E-commerce website.
* This coherent application is created using Django web framework.
* It is responsive website, so user can buy product using any device.<br /><br />

* To add new product or category browse `127.0.0.1:8000/add_product`.
* Login with Django admin site credentials.
* Product and category can be edited or removed using Django admin site.

### Instructions:
1. Install Django using the following command:
	```
	pip install Django
	```

2. Install Pillow (PIL fork) using the following command:
	```
	pip install Pillow
	```

3. To migrate the database, execute:
	```
	python manage.py makemigrations
	```
	```
	python manage.py migrate
	```

4. Create a user to login to the admin site:
	```
	python manage.py createsuperuser
	```

5. To run the program in local server:
	```
	python manage.py runserver
	```
