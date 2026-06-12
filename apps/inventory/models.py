from mongoengine import *
from apps.core.models import BaseDocument
from apps.products.models import Product

class InventoryMovement(BaseDocument):

    MOVEMENT_TYPES = (
        ('entry', 'Entrada'),
        ('exit', 'Salida'),
    )

    product = ReferenceField(Product)

    movement_type = StringField(
        choices=MOVEMENT_TYPES
    )

    quantity = IntField()

    meta = {
        'collection': 'inventory_movements'
    }