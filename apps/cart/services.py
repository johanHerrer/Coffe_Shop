from .models import Cart, CartItem
from apps.products.models import Product

class CartService:

    @staticmethod
    def add_product(user_id, product_id):

        cart = Cart.objects(
            user_id=user_id
        ).first()

        if not cart:

            cart = Cart(
                user_id=user_id
            )

        product = Product.objects(
            id=product_id
        ).first()

        found = False

        for item in cart.items:

            if str(item.product.id) == str(product.id):

                item.quantity += 1

                found = True

                break

        if not found:

            cart.items.append(
                CartItem(
                    product=product,
                    quantity=1
                )
            )

        cart.calculate_total()

        cart.save()

        return cart