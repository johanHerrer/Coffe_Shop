from django.urls import path
from .api import cart_api

urlpatterns = [
    path('', cart_api, name='cart_api')
]
