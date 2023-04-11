from django.db import models

# Create your models here.

class Cart(models.Model):
    cardID=models.IntegerField()
    # date_created=models.DateField(default="11/04/2023")
    customerID=models.IntegerField(default=1)




class Product(models.Model):
    product_name=models.CharField(max_length=100)
    product_quantity=models.IntegerField()
    product_price=models.IntegerField()

    def __str__(self) -> str:
        return self.product_name       
class Customer(Cart):
    customer_name=models.CharField(max_length=100)
    email=models.EmailField()
    def __str__(self) -> str:
        return f'{self.cardID}s cart'
