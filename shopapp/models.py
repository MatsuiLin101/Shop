from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=False)
    price = models.IntegerField(null=False)
    inventory = models.IntegerField(null=False)
    description = models.TextField(default="No description")
    img = models.URLField(null=False)
#    img = models.ImageField(upload_to='shopapp/', null=False)

    def __str__(self):
        return self.name

class Order(models.Model):

    PAYCARD = "CARD"
    PAYPOD = "POD"
    PAY_CHOICES = {
        (PAYCARD, "PayCard"),
        (PAYPOD, "PayPOD"),
    }

    PENDING = 1
    PROCESSING = 2
    ONTHEWAY = 3
    DELIVERED = 4
    STATUS_CHOICES = {
        (PENDING, "Pending"),
        (PROCESSING, "Processing"),
        (ONTHEWAY, "On the Way"),
        (DELIVERED, "Delivered"),
    }

    name = models.ForeignKey(User, on_delete=models.CASCADE)
    oid = models.CharField(max_length=20, null=False)
    order_name = models.CharField(max_length=20, null=False)
    order_tel = models.PositiveIntegerField()
    order_address = models.CharField(max_length=100, null=False)
    pay = models.CharField(max_length=10, choices=PAY_CHOICES)
    status = models.IntegerField(choices=STATUS_CHOICES)
    total = models.IntegerField(default=0, null=False)
    order_date = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.oid

class OrderItem(models.Model):
    oid = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    subtotal = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.oid.oid
