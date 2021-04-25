from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=100, null=False)

	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField(max_length=100, null=False)
	category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
	price = models.IntegerField(null=False)
	discount = models.IntegerField(null=False, default=0)
	desc = models.TextField(null=True)

	def __str__(self):
		return self.name
