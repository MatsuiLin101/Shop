"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from shopapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('category/<str:category>', views.shop_category, name="shop-category"),
    path('dashboard/', views.admin_dashboard, name="admin-dashboard"),
    path('dashboard/<str:category>', views.dashboard_category, name="dashboard-category"),
    path('dashboard/add_category/', views.add_category, name="add-category"),
    path('dashboard/add_product/', views.add_product, name="add-product"),
    path('dashboard/edit_category/<int:id>', views.edit_category, name="edit-category"),
    path('dashboard/edit_product/<int:id>', views.edit_product, name="edit-product"),
    path('dashboard/delete_category/<int:id>', views.delete_category, name="delete-category"),
    path('dashboard/delete_product/<int:id>', views.delete_product, name="delete-product"),
    path('detail/<int:id>', views.detail_product, name="detail-product"),
    path('cart/', views.cart, name='cart'),
    path('add_cart/<int:pid>/<int:quantity>', views.add_cart, name="add-cart"),
    path('del_cart/<int:pid>', views.del_cart, name="del-cart"),
    path('edit_cart/<int:pid>/<int:qty>', views.edit_cart, name="edit-cart"),
    path('order/', views.order, name="order"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('sign_up/', views.sign_up, name='sign-up'),
    path('account/', views.account_center, name='account-center'),
    path('account/<int:oid>', views.account_order, name='account-order'),
    path('order_list/', views.order_list, name='order-list'),
    path('order_detail/<int:oid>', views.order_detail, name='order-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
