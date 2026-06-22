from django.shortcuts import render, redirect
from .forms import CheckoutForm
from .services import OrderService
from .models import Order
from apps.users.decorators import admin_required


def checkout(request):
    user_id = request.session.get("user_id")

    if not user_id:
        return redirect('login')

    form = CheckoutForm()

    if request.method == "POST":
        form = CheckoutForm(request.POST)

        if form.is_valid():
            order = OrderService.create_order(
                user_id,
                form.cleaned_data["address"]
            )
            return redirect(
                "order_detail",
                order.id
            )

    return render(
        request,
        "orders/checkout.html",
        {
            "form": form
        }
    )


def order_detail(request, id):
    order = Order.objects(id=id).first()

    if not order:
        return redirect('home')

    return render(
        request,
        "orders/detail.html",
        {
            "order": order
        }
    )

@admin_required
def dashboard_orders(request):
    orders = Order.objects()
    return render(request, "dashboard/orders.html", {"orders": orders})