from mongoengine import *
from apps.core.models import BaseDocument
from apps.users.models import User
from apps.products.models import Product

class OrderItem(EmbeddedDocument):

    product = ReferenceField(Product)

    quantity = IntField(default=1)

    price = FloatField()


    @property
    def subtotal(self):
        return self.quantity * self.price


class Order(BaseDocument):


    STATUS = (

        "Pendiente",
        "Preparando",
        "En camino",
        "Entregado",
        "Cancelado"

    )


    user_id = StringField(required=True)


    items = EmbeddedDocumentListField(
        OrderItem
    )


    total = FloatField(
        default=0
    )


    status = StringField(
        default="Pendiente"
    )


    payment_status = StringField(
        default="Pendiente"
    )


    address = StringField()



    def calculate_total(self):

        total = 0

        for item in self.items:

            total += item.subtotal()


        self.total = total