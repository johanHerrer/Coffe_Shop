from mongoengine import *
from apps.core.models import BaseDocument
from apps.users.models import User
from apps.products.models import Product

class OrderItem(EmbeddedDocument):

    product = ReferenceField(Product)

    quantity = IntField()

    price = FloatField()

class Order(BaseDocument):

    STATUS_CHOICES = (
        ('pending', 'Pendiente'),
        ('preparing', 'Preparando'),
        ('delivered', 'Entregado'),
    )

    user = ReferenceField(User)

    items = EmbeddedDocumentListField(OrderItem)

    total = FloatField()

    status = StringField(
        choices=STATUS_CHOICES,
        default='pending'
    )

    meta = {
        'collection': 'orders'
    }