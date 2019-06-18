from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=155, unique=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=155, unique=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	nutriscore = models.IntegerField()
	url = models.CharField(max_length=255, default="")
	image_url = models.CharField(max_length=255, default="")
	salt = models.FloatField(default=0)
	sugar = models.FloatField(default=0)
	calories = models.FloatField(default=0)
	fat = models.FloatField(default=0)

	def __str__(self):
		return self.name

class Alternative(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
