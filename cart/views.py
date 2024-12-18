from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST, require_GET
from django.contrib import messages
from django.utils.translation import gettext as _

from .cart import Cart
from .forms import AddToCartProductForm
from products.models import Product


def cart_detail_view(request):
    cart = Cart(request)

    for item in cart:
        item['product_update_quantity_form'] = AddToCartProductForm(initial={
            'quantity': item['quantity'],
            'inplace': True
        })

    return render(request, 'cart/cart.html', {'cart': cart})


@require_POST
def add_to_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    quantity_form = AddToCartProductForm(request.POST)

    if quantity_form.is_valid():
        cleaned_data = quantity_form.cleaned_data
        quantity = cleaned_data['quantity']
        replace_current_quantity = cleaned_data['inplace']
        cart.add(product, quantity, replace_current_quantity)
        messages.success(request, _('Product successfully added to cart.'))

        return redirect('cart:cart_detail')


def remove_from_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    cart.remove(product)
    messages.error(request, _('Product successfully removed from cart.'))

    return redirect('cart:cart_detail')


def clear_cart_view(request):
    cart = Cart(request)
    cart.clear()
    messages.warning(request, _('Cart was cleared.'))

    return redirect('product_list')
