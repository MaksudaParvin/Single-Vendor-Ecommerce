from django.shortcuts import redirect


def process_payment(request, order_id):
    return redirect(
        "orders:order_success",
        order_id=order_id
    )