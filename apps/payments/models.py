from mongoengine import *
from apps.core.models import BaseDocument


class Payment(BaseDocument):

    amount = FloatField(required=True)

    currency = StringField(default='USD')

    status = StringField(default='Pendiente')

    method = StringField()

    order_id = StringField(required=False)

    user_id = StringField(required=False)

    meta = {
        'collection': 'payments'
    }

    def __str__(self):
        return f'Payment {self.id} - {self.status}'
