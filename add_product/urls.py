from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
	path('logout', views.logout, name='logout'),
	path('add_product', views.add_product, name='add_product'),
	path('add_category', views.add_category, name='add_category')
]
