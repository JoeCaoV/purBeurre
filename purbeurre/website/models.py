from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=155)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=155)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	nutriscore = models.IntegerField()

	def __str__(self):
		return self.name

class Alternative(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
