from django.shortcuts import render

from . import models

# Create your views here.

def home(request):

    products = models.Product.objects.all()

    return render(request, 'shopapp/home.html', locals())

def add_item(request):

    return render(request, 'shopapp/add_item.html', locals())
