from django.db import models

# Create your models here.
class Products(models.Model):
    product_name=models.CharField(max_length=100)
    product_quantity=models.IntegerField()
    product_price=models.IntegerField()
    