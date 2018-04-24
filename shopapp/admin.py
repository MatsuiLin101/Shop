from django.contrib import admin

from . import models

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
