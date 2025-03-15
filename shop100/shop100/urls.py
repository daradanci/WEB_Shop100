
from django.contrib import admin
from django.urls import path
from shop100app.views import clothes_list, clothes_detail, cart_detail
from django.urls import path

urlpatterns = [
    path('', clothes_list, name='clothes_list'),  # Главная страница со списком товаров
    path('clothes/<int:clothes_id>/', clothes_detail, name='clothes_detail'),  # Детальная страница товара
    path('cart/', cart_detail, name='cart_detail'),  # Страница корзины
]
