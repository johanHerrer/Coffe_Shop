from django.urls import path
from .api import payments_api

urlpatterns = [
    path('', payments_api, name='payments_api')
]
