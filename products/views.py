from django.shortcuts import render, reverse
from django.views import generic
from django.urls import reverse_lazy

from .models import Product


class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(generic.CreateView):
    model = Product
    fields = ['title', 'body', 'price', 'active']
    template_name = 'products/product_create.html'
    context_object_name = 'form'


class ProductUpdateView(generic.UpdateView):
    model = Product
    fields = ['title', 'body', 'price', 'active']
    template_name = 'products/product_update.html'
    context_object_name = 'form'


class ProductDeleteView(generic.DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product_list')

