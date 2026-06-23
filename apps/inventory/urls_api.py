from django.urls import path
from .api import inventory_api

urlpatterns = [
    path('', inventory_api, name='inventory_api')
]
