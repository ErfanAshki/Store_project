from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class Product(models.Model):
    CATEGORY_CHOICES = (
        ('Men shoes', 'Men shoes'),
        ('Women shoes', 'Women shoes')
    )
    title = models.CharField(max_length=150)
    body = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    price = models.PositiveIntegerField(default=100)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='shoes_pic', null=True, blank=True)
    is_pay = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    publisher = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])


