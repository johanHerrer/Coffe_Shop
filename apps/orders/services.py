from .models import Order, OrderItem
from apps.cart.models import Cart



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



        order.calculate_total()


        order.save()


        cart.delete()



        return order