from mongoengine import *
from apps.core.models import BaseDocument
from apps.products.models import Product
from apps.users.models import User

class CartItem(EmbeddedDocument):

    product = ReferenceField(Product)

    quantity = IntField(default=1)

    subtotal = FloatField(default=0)

    def calculate_subtotal(self):
        self.subtotal = (
            self.product.price * self.quantity
        )

class Cart(BaseDocument):

    user_id = StringField(required=True)

    items = EmbeddedDocumentListField(CartItem)

    total = FloatField(default=0)

    meta = {
        "collection": "carts"
    }

    def calculate_total(self):

        total = 0

        for item in self.items:

            item.calculate_subtotal()

            total += item.subtotal

        self.total = total