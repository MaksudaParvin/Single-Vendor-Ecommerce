from django.shortcuts import render, redirect


from decimal import Decimal

from django.shortcuts import get_object_or_404, redirect, render

from products.models import Product


def cart_view(request):

    cart = request.session.get("cart", {})

    cart_items = []

    subtotal = Decimal("0.00")

    for product_id, quantity in cart.items():

        product = get_object_or_404(
            Product,
            id=product_id
        )

        quantity = int(quantity)

        total_price = product.price * quantity

        subtotal += total_price

        cart_items.append({
            "product": product,
            "quantity": quantity,
            "total_price": total_price,
        })


    context = {
        "cart_items": cart_items,
        "subtotal": subtotal,
    }

    return render(
        request,
        "cart/cart.html",
        context
    )


def add_to_cart(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    cart = request.session.get("cart", {})

    product_id = str(product_id)

    current_quantity = int(
        cart.get(product_id, 0)
    )

    if current_quantity < product.quantity:

        cart[product_id] = current_quantity + 1

    request.session["cart"] = cart

    request.session.modified = True

    return redirect(
        request.META.get(
            "HTTP_REFERER",
            "/products/"
        )
    )


def increase_quantity(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    cart = request.session.get("cart", {})

    product_id = str(product_id)

    current_quantity = int(
        cart.get(product_id, 0)
    )

    if current_quantity < product.quantity:

        cart[product_id] = current_quantity + 1

    request.session["cart"] = cart

    request.session.modified = True

    return redirect("cart:cart")


def decrease_quantity(request, product_id):

    cart = request.session.get("cart", {})

    product_id = str(product_id)

    if product_id in cart:

        current_quantity = int(
            cart[product_id]
        )

        if current_quantity > 1:

            cart[product_id] = current_quantity - 1

        else:

            del cart[product_id]


    request.session["cart"] = cart

    request.session.modified = True

    return redirect("cart:cart")


def remove_from_cart(request, product_id):

    cart = request.session.get("cart", {})

    product_id = str(product_id)

    if product_id in cart:

        del cart[product_id]


    request.session["cart"] = cart

    request.session.modified = True

    return redirect("cart:cart")