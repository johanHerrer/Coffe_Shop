from django.urls import path
from .api import dashboard_api

urlpatterns = [
    path('', dashboard_api, name='dashboard_api')
]
