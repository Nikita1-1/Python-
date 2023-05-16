from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=250)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url



class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=80)

    @property
    def cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.get_total() for item in order_items])
        return total

    @property
    def cart_quantity(self):
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total

class OrderItem(models.Model):
    quantity = models.IntegerField(default=0, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def get_total(self):
        total = self.quantity * self.product.price
        return total




#creating comments
# class Comments(models.Model):
#     #стандартная модель в джанго
#     # это любой зарегестрированный пользоатель
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.TextField()
#     #to make autofill of data we create auto_now_add = True
#     created_at = models.DateTimeField(auto_now_add=True)
