from django.shortcuts import render, reverse
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin

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


class ProductCreateView(UserPassesTestMixin, generic.CreateView):
    model = Product
    fields = ['title', 'body', 'price', 'image']
    template_name = 'products/product_create.html'
    context_object_name = 'form'

    def test_func(self):
        obj = self.get_object()
        return obj.publisher == self.request.user


class ProductUpdateView(UserPassesTestMixin, generic.UpdateView):
    model = Product
    fields = ['title', 'body', 'price', 'image']
    template_name = 'products/product_update.html'
    context_object_name = 'form'

    def test_func(self):
        obj = self.get_object()
        return obj.publisher == self.request.user


class ProductDeleteView(UserPassesTestMixin, generic.DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product_list')

    def test_func(self):
        obj = self.get_object()
        return obj.publisher == self.request.user

