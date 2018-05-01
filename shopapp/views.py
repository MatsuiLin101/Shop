from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

from . import models, forms

import random, string

# Create your views here.

def home(request):

#    if "cart" in request.session:
#        del request.session["cart"]

    categories = models.Category.objects.all()
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

        return redirect(admin_dashboard)
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

                    return redirect(admin_dashboard)
            except:
                message = "Please input category name or the name is exsits."

                return render(request, 'shopapp/add_category.html', {"message":message})
    else:
        form = forms.CategoryForm()

    return render(request, 'shopapp/add_category.html', locals())

def shop_category(request, category):

    category = models.Category.objects.get(name=category)
    categories = models.Category.objects.all()
    products = models.Product.objects.filter(category=category)

    return render(request, 'shopapp/shop_category.html', locals())

def admin_dashboard(request):

    categories = models.Category.objects.all()
    products = models.Product.objects.all()

    return render(request, 'shopapp/admin_dashboard.html', locals())

def dashboard_category(request, category):

    category = models.Category.objects.get(name=category)
    categories = models.Category.objects.all()
    products = models.Product.objects.filter(category=category)

    return render(request, 'shopapp/dashboard_category.html', locals())

def edit_category(request, id):

    category = models.Category.objects.get(id=id)

    if request.method == "POST":
        category.name = request.POST["name"]
        category.save()

        return redirect(admin_dashboard)

    return render(request, 'shopapp/edit_category.html', locals())

def edit_product(request, id):

    product = models.Product.objects.get(id=id)

    if request.method == "POST":
        form = forms.ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(admin_dashboard)
    else:
        form = forms.ProductForm(instance=product)

    return render(request, 'shopapp/edit_product.html', locals())

def delete_category(request, id):

    category = models.Category.objects.get(id=id)
    category.delete()

    return redirect(admin_dashboard)

def delete_product(request, id):

    product = models.Product.objects.get(id=id)
    product.img.delete(save=True)
    product.delete()

    return redirect(admin_dashboard)

def detail_product(request, id):

    categories = models.Category.objects.all()
    product = models.Product.objects.get(id=id)

    return render(request, 'shopapp/detail_product.html', locals())

def cart(request):
    if "cart" in request.session:
        carts = request.session["cart"]
    else:
        message = "No product in cart"

        return render(request, 'shoaapp/cart.html', locals())

    total = 0
    products = []
    for c in carts:
        product = models.Product.objects.get(id=c[0])
        img = product.img
        quantity = product.quantity
        price = product.price
        subtotal = price * c[1]
        total += subtotal
        pid = product.id
        products.append([img, product, quantity, price, c[1], subtotal, pid])

    return render(request, 'shopapp/cart.html', locals())

def add_cart(request, pid, quantity):

    if not "cart" in request.session:
        cart = [pid, quantity]
        carts = []
        carts.append(cart)
        request.session["cart"] = carts
        message = "add to cart"
    else:
        carts = request.session["cart"]

        for c in carts:
            if c[0] == pid:
                c[1] = c[1] + quantity
                message = "add to cart"
                request.session["cart"] = carts

                return HttpResponse(message)

        cart = [pid, quantity]
        carts.append(cart)
        request.session["cart"] = carts
        message = "add to cart"

    return HttpResponse(message)

def edit_cart(request, pid, qty):

    carts = request.session["cart"]
    for c in carts:
        if c[0] == pid:
            if qty == 1:
                c[1] = c[1] + qty
                message = "edit add qty"
            else:
                c[1] = c[1] - 1
                message = "edit minus qty"
            request.session["cart"] = carts

            return HttpResponse(message)

    message = "edit error"

    return HttpResponse(message)

def del_cart(request, pid):

    carts = request.session["cart"]
    new_carts = []
    for c in carts:
        if c[0] != pid:
            new_carts.append(c)
    request.session["cart"] = new_carts
    message = "del product"

    return HttpResponse(message)

def order(request):

    if request.method == "POST":
        order = request.POST
        order_pay = request.POST["order-pay"]
        order_name = request.POST["order-name"]
        order_tel = request.POST["order-tel"]
        order_address = request.POST["order-address"]
        pid = request.POST.getlist("pid")
        qty = request.POST.getlist("qty")
        products = []
        for i in range(len(pid)):
            product = []
            product = [pid[i], qty[i]]
            products.append(product)

    return render(request, 'shopapp/order.html', locals())
