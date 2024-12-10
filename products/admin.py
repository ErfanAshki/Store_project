from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    ordering = ['-id']
    list_display = ['id', 'title', 'price', 'category', 'is_pay', 'active', 'datetime_created']


admin.site.register(Product, ProductAdmin)
