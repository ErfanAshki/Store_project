from django.contrib import admin

from .models import Product, Comment


class ProductAdmin(admin.ModelAdmin):
    ordering = ['-id']
    list_display = ['id', 'title', 'price', 'category', 'is_pay', 'active', 'datetime_created']


admin.site.register(Product, ProductAdmin)


class CommentAdmin(admin.ModelAdmin):
    ordering = ['-id']
    list_display = ['id', 'text', 'author', 'product', 'stars', 'active', 'datetime_created']


admin.site.register(Comment, CommentAdmin)
