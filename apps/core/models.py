from mongoengine import *
from datetime import datetime

class BaseDocument(Document):

    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'abstract': True
    }

    def save(self, *args, **kwargs):

        self.updated_at = datetime.utcnow()

        return super().save(*args, **kwargs)