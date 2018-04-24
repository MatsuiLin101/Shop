from django import forms

from . import models

class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ("name",)

class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ("category", "name", "price", "quantity", "description", "img")
