from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=200)

class Product(models.Model):
	name = models.CharField(max_length=250)
	cost = models.DecimalField(max_digits=8,decimal_places=2)
	category = models.ForeignKey(Category,on_delete=models.PROTECT)
	
class SalesOrder(models.Model):
	description = models.CharField(max_length=600)
	products = models.ManyToManyField(Product)







