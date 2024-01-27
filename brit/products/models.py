
from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=1024, verbose_name="product_name")
    price = models.IntegerField(verbose_name="product_price")