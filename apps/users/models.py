from mongoengine import *
from apps.core.models import BaseDocument

class Role(BaseDocument):

    name = StringField(
        required=True,
        unique=True
    )

    description = StringField()

    meta = {
        'collection': 'roles'
    }

    def __str__(self):
        return self.name
    
class User(BaseDocument):

    full_name = StringField(required=True)

    email = EmailField(
        required=True,
        unique=True
    )

    password = StringField(required=True)

    phone = StringField()

    role = ReferenceField(Role)

    is_active = BooleanField(default=True)

    meta = {
        'collection': 'users'
    }

    def __str__(self):
        return self.full_name