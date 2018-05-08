from django.contrib import admin

from . import models

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('oid', 'name', 'status', 'order_date')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('oid', 'product', 'price', 'quantity')


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderItem, OrderItemAdmin)
