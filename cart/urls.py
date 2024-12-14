from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
   path('', views.cart_detail_view, name='cart_detail'),
   path('<int:product_id>/add/', views.add_to_cart_view, name='cart_add'),

]
