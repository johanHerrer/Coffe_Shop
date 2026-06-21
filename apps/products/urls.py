from django.urls import path
from .views import *

urlpatterns = [

    path(
        '',
        products_list,
        name='products'
    ),

    path(
        'create/',
        create_product,
        name='create_product'
    ),

    path(
        'delete/<str:product_id>/',
        delete_product,
        name='delete_product'
    ),

    path(
        'dashboard/',
        dashboard_products,
        name='dashboard_products'
    ),
]