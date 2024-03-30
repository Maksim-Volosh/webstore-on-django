from django.contrib import admin
from django.urls import include, path

from goods.views import *

app_name = 'goods'

urlpatterns = [
    path('<slug:cat_slug>', catalog, name="index"),
    path('product/<slug:product_slug>', product, name='product'),
]
