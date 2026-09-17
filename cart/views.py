from django.shortcuts import render, redirect


def cart_view(request):
    return render(request, "cart/cart.html")


def add_to_cart(request, product_id):
    return redirect("cart:cart")


def increase_quantity(request, product_id):
    return redirect("cart:cart")


def decrease_quantity(request, product_id):
    return redirect("cart:cart")


def remove_from_cart(request, product_id):
    return redirect("cart:cart")