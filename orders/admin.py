from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    fields = list_display = ['id', 'order', 'product', 'quantity']
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'user', 'first_name', 'last_name', 'phone_number', 'datetime_created', 'is_paid']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'order', 'product', 'quantity']


admin.site.register(OrderItem, OrderItemAdmin)
