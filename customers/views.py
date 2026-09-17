from django.contrib import messages
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from products.models import Product
from .models import Customer
from orders.models import Order, OrderItem


def checkout(request):

    cart = request.session.get("cart", {})

    # Empty cart
    if not cart:
        return redirect("cart:cart")

    cart_items = []
    subtotal = 0

    # =========================================
    # GET CART PRODUCTS
    # =========================================

    for product_id, quantity in cart.items():

        product = get_object_or_404(
            Product,
            id=product_id,
            is_active=True
        )

        quantity = int(quantity)

        # Check stock
        if quantity > product.quantity:

            messages.error(
                request,
                f"Only {product.quantity} units of "
                f"{product.name} are available."
            )

            return redirect("cart:cart")

        item_total = product.price * quantity

        cart_items.append({
            "product": product,
            "quantity": quantity,
            "price": product.price,
            "total_price": item_total,
        })

        subtotal += item_total


    # =========================================
    # PLACE ORDER
    # =========================================

    if request.method == "POST":

        name = request.POST.get(
            "name",
            ""
        ).strip()

        phone = request.POST.get(
            "phone",
            ""
        ).strip()

        address = request.POST.get(
            "address",
            ""
        ).strip()

        payment_method = request.POST.get(
            "payment_method",
            "cod"
        )


        # =====================================
        # VALIDATION
        # =====================================

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


        if payment_method != "cod":

            messages.error(
                request,
                "Please select Cash on Delivery."
            )

            return render(
                request,
                "customers/checkout.html",
                {
                    "cart_items": cart_items,
                    "subtotal": subtotal,
                }
            )


        # =====================================
        # CREATE ORDER + ORDER ITEMS
        # =====================================

        with transaction.atomic():

            # Create customer
            customer = Customer.objects.create(
                name=name,
                phone=phone,
                address=address,
            )


            # Create main Order
            order = Order.objects.create(
                customer=customer,
                total_price=subtotal,
                status=Order.Status.PENDING,
            )


            # Create OrderItems
            for item in cart_items:

                product = Product.objects.select_for_update().get(
                    id=item["product"].id
                )

                quantity = item["quantity"]

                # Final stock check
                if quantity > product.quantity:

                    messages.error(
                        request,
                        f"Not enough stock for "
                        f"{product.name}."
                    )

                    return redirect("cart:cart")


                item_total = product.price * quantity


                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    price=product.price,
                    total_price=item_total,
                )


                # Reduce stock
                product.quantity -= quantity

                product.save(
                    update_fields=["quantity"]
                )


        # =====================================
        # CLEAR CART
        # =====================================

        request.session["cart"] = {}

        request.session.modified = True


        # =====================================
        # SUCCESS MESSAGE
        # =====================================

        messages.success(
            request,
            "Order placed successfully!"
        )


        return redirect(
            "orders:order_success",
            order_id=order.id
        )


    # =========================================
    # CHECKOUT PAGE
    # =========================================

    return render(
        request,
        "customers/checkout.html",
        {
            "cart_items": cart_items,
            "subtotal": subtotal,
        }
    )