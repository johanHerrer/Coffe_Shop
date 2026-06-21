from django.urls import path
from .views import cart_view, add_to_cart, remove_from_cart, decrement_cart_item

urlpatterns = [
    path(
        '',
        cart_view,
        name='cart'
    ),
    path(
        'add/<str:product_id>/',
        add_to_cart,
        name='add_to_cart'
    ),
    path(
        'decrement/<str:product_id>/',
        decrement_cart_item,
        name='decrement_cart_item'
    ),
    path(
        'remove/<str:product_id>/',
        remove_from_cart,
        name='remove_from_cart'
    ),
]