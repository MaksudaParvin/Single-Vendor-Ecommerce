from django.shortcuts import render


def order_success(request, order_id):
    return render(
        request,
        "orders/order_success.html",
        {
            "order_id": order_id
        }
    )