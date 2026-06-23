from .models import Order, OrderItem
from apps.cart.models import Cart
from apps.products.models import Product


class OrderService:

    @staticmethod
    def create_order(
        user_id,
        address
    ):

        cart = Cart.objects(
            user_id=user_id
        ).first()

        order = Order(
            user_id=user_id,
            address=address
        )

        for item in cart.items:
            order.items.append(
                OrderItem(
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )
            )

            # Decrement stock for non-on-demand products
            if not item.product.is_on_demand:
                product = Product.objects(id=item.product.id).first()
                if product:
                    product.stock -= item.quantity
                    if product.stock < 0:
                        product.stock = 0
                    product.save()

        order.calculate_total()
        order.save()
        cart.delete()

        return order