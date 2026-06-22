from django.urls import path

from .views import *


urlpatterns = [
    path("checkout/", checkout, name="checkout"),
    path("detail/<str:id>/", order_detail, name="order_detail"),
    path('dashboard/', dashboard_orders, name='dashboard_orders'),
]