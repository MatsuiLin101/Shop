from django.shortcuts import render

from . import models

# Create your views here.

def home(request):

    products = models.Product.objects.all()

    return render(request, 'shopapp/home.html', locals())
