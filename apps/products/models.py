from mongoengine import *
from apps.core.models import BaseDocument
from slugify import slugify

class Category(BaseDocument):

    name = StringField(
        required=True,
        unique=True
    )

    slug = StringField(unique=True)

    meta = {
        'collection': 'categories'
    }

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(BaseDocument):

    name = StringField(required=True)

    slug = StringField(unique=True)

    description = StringField()

    price = FloatField(required=True)

    stock = IntField(default=0)

    image = StringField()

    available = BooleanField(default=True)

    featured = BooleanField(default=False)

    category = ReferenceField(Category)

    meta = {
        'collection': 'products'
    }

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name