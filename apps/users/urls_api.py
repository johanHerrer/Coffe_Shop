from django.urls import path
from .api import users_api

urlpatterns = [
    path('', users_api, name='users_api')
]
