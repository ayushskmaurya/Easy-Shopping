from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
	path('search/<query>', views.searched, name='searched'),
	path('category/<category_id>', views.category, name='category'),
	path('product/<product_id>', views.product, name='product'),
	path('add_to_cart/<product_id>', views.add_to_cart, name='add_to_cart'),
	path('add_to_wishlist/<product_id>', views.add_to_wishlist, name='add_to_wishlist'),
	path('verify_user', views.verify_user, name='verify_user'),
	path('validate_user', views.validate_user, name='validate_user'),
	path('signout', views.signout, name='signout')
]
