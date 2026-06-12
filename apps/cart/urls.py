from django.urls import path
from .views import *

urlpatterns = [

    path(
        'add/<str:product_id>/',
        add_to_cart,
        name='add_to_cart'
    )
]