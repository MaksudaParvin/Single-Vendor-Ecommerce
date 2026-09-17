from django.shortcuts import render


from django.contrib import messages
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from products.models import Product
from .models import Customer
from orders.models import Order


def checkout(request):

    cart = request.session.get("cart", {})

    # Empty cart হলে Cart page-এ পাঠাবে
    if not cart:
        return redirect("cart:cart")

    cart_items = []
    subtotal = 0

    # Cart products
    for product_id, quantity in cart.items():

        product = get_object_or_404(
            Product,
            id=product_id,
            is_active=True
        )

        quantity = int(quantity)

        # Stock check
        if quantity > product.quantity:
            messages.error(
                request,
                f"Only {product.quantity} units of {product.name} are available."
            )
            return redirect("cart:cart")

        total_price = product.price * quantity

        cart_items.append({
            "product": product,
            "quantity": quantity,
            "total_price": total_price,
        })

        subtotal += total_price


    # ==============================
    # PLACE ORDER
    # ==============================

    if request.method == "POST":

        name = request.POST.get("name", "").strip()
        phone = request.POST.get("phone", "").strip()
        address = request.POST.get("address", "").strip()
        payment_method = request.POST.get(
            "payment_method",
            "cod"
        )

        # Validation
        if not name or not phone or not address:

            messages.error(
                request,
                "Please fill in all required fields."
            )

            return render(
                request,
                "customers/checkout.html",
                {
                    "cart_items": cart_items,
                    "subtotal": subtotal,
                }
            )


        # Currently only COD
        if payment_method != "cod":

            messages.error(
                request,
                "Please select a valid payment method."
            )

            return render(
                request,
                "customers/checkout.html",
                {
                    "cart_items": cart_items,
                    "subtotal": subtotal,
                }
            )


        # ==============================
        # SAVE ORDER
        # ==============================

        with transaction.atomic():

            customer = Customer.objects.create(
                name=name,
                phone=phone,
                address=address,
            )


            for item in cart_items:

                product = item["product"]
                quantity = item["quantity"]
                total_price = item["total_price"]

                # Final stock check
                product = Product.objects.select_for_update().get(
                    id=product.id
                )

                if quantity > product.quantity:

                    messages.error(
                        request,
                        f"Not enough stock for {product.name}."
                    )

                    return redirect("cart:cart")


                Order.objects.create(
                    customer=customer,
                    product=product,
                    quantity=quantity,
                    total_price=total_price,
                )


                # Reduce stock
                product.quantity -= quantity
                product.save(
                    update_fields=["quantity"]
                )


        # Empty cart
        request.session["cart"] = {}
        request.session.modified = True


        # Success page
        return redirect("orders:order_success")


    # ==============================
    # CHECKOUT PAGE
    # ==============================

    return render(
        request,
        "customers/checkout.html",
        {
            "cart_items": cart_items,
            "subtotal": subtotal,
        }
    )