from django.contrib import admin
from .models import Category, Product, OnlineShopUser, Cart, Wishlist, Order

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(OnlineShopUser)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Order)
