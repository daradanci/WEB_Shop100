from django.contrib import admin
from django.urls import path
from shop100app.views import clothes_list, clothes_detail, cart_detail, add_to_cart

urlpatterns = [
    path("", clothes_list, name="product_list"),  # <-- Здесь добавляем name="product_list"
    path("clothes/<int:clothes_id>/", clothes_detail, name="clothes_detail"),
    path("cart/", cart_detail, name="cart_detail"),
    path("cart/add/<int:product_id>/", add_to_cart, name="add_to_cart"),
]
