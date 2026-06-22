from django.urls import path

from .api import products_api



urlpatterns=[


    path(
        '',
        products_api,
        name="products_api"
    )

]