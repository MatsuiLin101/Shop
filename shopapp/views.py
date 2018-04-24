from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from . import models, forms

import random, string

# Create your views here.

def home(request):

    products = models.Product.objects.all()

    return render(request, 'shopapp/home.html', locals())

def add_product(request):

    if request.method == "POST":
        category = request.POST["category"]
        name = request.POST["name"]
        price = request.POST["price"]
        quantity = request.POST["quantity"]
        description = request.POST["description"]
        img_file = request.FILES["img"]
        img_name = request.FILES["img"].name
        img_path = "shopapp/" + img_name
        model_create = models.Product.objects.create(category=models.Category.objects.get(id=category), name=name, price=price, quantity=quantity, description=description)
        model_create.img = FileSystemStorage().save(img_path, img_file)
        model_create.save()

        return redirect(home)
    else:
        form = forms.ProductForm()

    return render(request, 'shopapp/add_product.html', locals())

def add_category(request):

    if request.method == "POST":
        form = forms.CategoryForm(request.POST)

        try:
            category = models.Category.objects.get(name=request.POST["name"])
            message = "Please input category name or the name is exsits."

            return render(request, 'shopapp/add_category.html', {"message":message})
        except:
            try:
                if form.is_valid:
                    form.save()

                    return redirect(home)
            except:
                message = "Please input category name or the name is exsits."

                return render(request, 'shopapp/add_category.html', {"message":message})
    else:
        form = forms.CategoryForm()

    return render(request, 'shopapp/add_category.html', locals())
