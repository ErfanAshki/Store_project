from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, verbose_name=_('first_name'))
    last_name = models.CharField(max_length=50, verbose_name=_('last_name'))
    phone_number = PhoneNumberField(unique=True, verbose_name=_('phone_number'))
    address = models.CharField(max_length=200, verbose_name=_('address'))
    notes = models.TextField(blank=True, null=True, verbose_name=_('notes'))
    datetime_created = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} --> {self.user}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"order_item {self.id} : {self.product} * {self.quantity}"

