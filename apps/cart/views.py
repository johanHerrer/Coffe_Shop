from django.shortcuts import redirect, render
from .models import Cart
from .services import CartService


def cart_view(request):
    user_id = request.session.get('user_id')
    cart = Cart.objects(user_id=user_id).first() if user_id else None

    return render(
        request,
        'cart/cart.html',
        {
            'cart': cart
        }
    )


def add_to_cart(request, product_id):
    user_id = request.session.get('user_id')

    if user_id:
        CartService.add_product(user_id, product_id)

    return redirect(request.META.get('HTTP_REFERER', '/'))


def decrement_cart_item(request, product_id):
    user_id = request.session.get('user_id')

    if user_id:
        CartService.decrement_product(user_id, product_id)

    return redirect('cart')


def remove_from_cart(request, product_id):
    user_id = request.session.get('user_id')

    if user_id:
        CartService.remove_product(user_id, product_id)

    return redirect('cart')
