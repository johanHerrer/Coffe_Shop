import os
from uuid import uuid4
from django.conf import settings
from .models import Product

class ProductService:

    @staticmethod
    def save_image(image):

        if not image:
            return None

        extension = image.name.split('.')[-1]

        filename = f"{uuid4()}.{extension}"

        path = os.path.join(
            settings.MEDIA_ROOT,
            'products',
            filename
        )

        os.makedirs(
            os.path.dirname(path),
            exist_ok=True
        )

        with open(path, 'wb+') as destination:

            for chunk in image.chunks():

                destination.write(chunk)

        return f"products/{filename}"

    @staticmethod
    def create_product(data, image=None):

        image_path = ProductService.save_image(image)

        product = Product(

            name=data['name'],
            description=data['description'],
            price=data['price'],
            stock=data['stock'],
            featured=data.get('featured', False),
            is_on_demand=data.get('is_on_demand', False),
            image=image_path
        )

        product.save()

        return product