from django.urls import path
from .api import orders_api

urlpatterns=[
    path('',orders_api)
]