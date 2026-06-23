from .models import Cart, CartItem
from apps.products.models import Product

class CartService:

    @staticmethod
    def add_product(user_id, product_id):
        cart = Cart.objects(user_id=user_id).first()

        if not cart:
            cart = Cart(user_id=user_id)

        product = Product.objects(id=product_id).first()

        if not product:
            return cart

        # Validate stock for non-on-demand products
        if not product.is_on_demand and product.stock <= 0:
            return cart  # Cannot add product without stock

        found = False

        for item in cart.items:
            if str(item.product.id) == str(product.id):
                # For non-on-demand products, check if adding would exceed stock
                if not product.is_on_demand and (item.quantity + 1) > product.stock:
                    return cart  # Cannot exceed available stock
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

    @staticmethod
    def decrement_product(user_id, product_id):
        cart = Cart.objects(user_id=user_id).first()

        if not cart:
            return None

        for item in list(cart.items):
            if str(item.product.id) == str(product_id):
                item.quantity -= 1
                if item.quantity <= 0:
                    cart.items.remove(item)
                break

        if not cart.items:
            cart.delete()
            return None

        cart.calculate_total()
        cart.save()

        return cart

    @staticmethod
    def remove_product(user_id, product_id):
        cart = Cart.objects(user_id=user_id).first()

        if not cart:
            return None

        for item in list(cart.items):
            if str(item.product.id) == str(product_id):
                cart.items.remove(item)
                break

        if not cart.items:
            cart.delete()
            return None

        cart.calculate_total()
        cart.save()

        return cart