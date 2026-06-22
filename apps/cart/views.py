from django.shortcuts import redirect, render
from .models import Cart
from .services import CartService
from django.http import HttpResponse


def cart_view(request):
    user_id = request.session.get('user_id')
    cart_user = request.session.get('cart_user')

    if not user_id:
        # ensure we have a session cart id for anonymous users
        if not cart_user:
            import uuid
            cart_user = str(uuid.uuid4())
            request.session['cart_user'] = cart_user
        user_lookup = cart_user
    else:
        user_lookup = user_id

    cart = Cart.objects(user_id=user_lookup).first()

    return render(request, 'cart/cart.html', {'cart': cart})


def add_to_cart(request, product_id):
    user_id = request.session.get('user_id')
    cart_user = request.session.get('cart_user')

    if not user_id:
        # create or reuse anonymous cart id
        if not cart_user:
            import uuid
            cart_user = str(uuid.uuid4())
            request.session['cart_user'] = cart_user
        user_lookup = cart_user
    else:
        user_lookup = user_id

    cart = CartService.add_product(user_lookup, product_id)

    # compute total item count
    total_items = 0
    if cart:
        for item in cart.items:
            total_items += int(item.quantity)

    return HttpResponse(str(total_items))


def decrement_cart_item(request, product_id):
    user_id = request.session.get('user_id')
    cart_user = request.session.get('cart_user')

    if not user_id and not cart_user:
        return redirect('cart')

    user_lookup = user_id if user_id else cart_user
    CartService.decrement_product(user_lookup, product_id)

    return redirect('cart')


def remove_from_cart(request, product_id):
    user_id = request.session.get('user_id')
    cart_user = request.session.get('cart_user')

    if not user_id and not cart_user:
        return redirect('cart')

    user_lookup = user_id if user_id else cart_user
    CartService.remove_product(user_lookup, product_id)

    return redirect('cart')
