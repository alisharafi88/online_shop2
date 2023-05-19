from django.shortcuts import render
from django.views import generic

from .models import ProductModel


class ProductListView(generic.ListView):
    model = ProductModel
    template_name = 'product/product_list.html'
    context_object_name = 'products'
