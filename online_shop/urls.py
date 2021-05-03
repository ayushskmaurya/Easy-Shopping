from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
	path('search/<query>', views.searched, name='searched'),
	path('category/<category_id>', views.category, name='category'),
	path('product/<product_id>', views.product, name='product'),

	path('cart', views.cart, name='cart'),
	path('add_to_cart/<product_id>', views.add_to_cart, name='add_to_cart'),
	path('delete_from_cart/<product_id>', views.delete_from_cart, name='delete_from_cart'),
	path('checkout', views.checkout, name='checkout'),

	path('add_to_wishlist/<product_id>', views.add_to_wishlist, name='add_to_wishlist'),

	path('verify_user', views.verify_user, name='verify_user'),
	path('validate_user', views.validate_user, name='validate_user'),
	path('signout', views.signout, name='signout')
]
