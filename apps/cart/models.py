from mongoengine import *
from apps.core.models import BaseDocument
from apps.products.models import Product
from apps.users.models import User

class CartItem(EmbeddedDocument):

    product = ReferenceField(Product)

    quantity = IntField(default=1)

class Cart(BaseDocument):

    user = ReferenceField(User)

    items = EmbeddedDocumentListField(CartItem)

    meta = {
        'collection': 'carts'
    }