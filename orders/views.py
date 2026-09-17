from django.shortcuts import render


from django.shortcuts import get_object_or_404, render

from .models import Order


def order_success(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id
    )

    return render(
        request,
        "orders/order_success.html",
        {
            "order": order,
        }
    )