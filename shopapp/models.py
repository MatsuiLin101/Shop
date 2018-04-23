from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=False)
    price = models.IntegerField(null=False)
    quantity = models.IntegerField(null=False)
    description = models.TextField(default="No description")
    img = models.ImageField(upload_to='shopapp/', null=False)

    def __str__(self):
        return self.name
