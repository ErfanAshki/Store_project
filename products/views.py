from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin

from .models import Product, Comment
from .forms import CommentForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        product_id = int(self.kwargs['pk'])
        return reverse('product_detail', args=[product_id])

    def form_valid(self, form):
        form_object = form.save(commit=False)
        form_object.author = self.request.user
        product_id = int(self.kwargs['pk'])
        product = get_object_or_404(Product, pk=product_id)
        form_object.product = product
        form_object.save()
        return super().form_valid(form)


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

