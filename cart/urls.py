from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
   path('', views.cart_detail_view, name='cart_detail'),
   path('<int:product_id>/add/', views.add_to_cart_view, name='cart_add'),
   path('<int:product_id>/remove/', views.remove_from_cart_view, name='cart_remove'),
   path('clear/', views.clear_cart_view, name='cart_clear'),

]
