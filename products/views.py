from django.shortcuts import render, reverse
from django.views import generic
from django.urls import reverse_lazy

from .models import Product


class ProductListView(generic.ListView):
    template_name = 'products/product_list_categories.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(id__in=[7, 17])


class MenProductListView(generic.ListView):
    template_name = 'products/product_men_list.html'
    context_object_name = 'products'
    paginate_by = 4

    def get_queryset(self):
        return Product.objects.filter(category='Men shoes')


class WomenProductListView(generic.ListView):
    template_name = 'products/product_women_list.html'
    context_object_name = 'products'
    paginate_by = 4

    def get_queryset(self):
        return Product.objects.filter(category='Women shoes')


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

