from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
	path('search/<query>', views.searched, name='searched'),
	path('category/<category_id>', views.category, name='category'),
	path('product/<product_id>', views.product, name='product'),
	path('verify_user', views.verify_user, name='verify_user'),
	path('validate_user', views.validate_user, name='validate_user'),
	path('signout', views.signout, name='signout')
]
