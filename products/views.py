from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def home(request):
    categories = Category.objects.all()

    featured_products = (
        Product.objects
        .filter(
            is_active=True,
            is_featured=True,
            quantity__gt=0
        )
        .select_related("category")
    )

    latest_products = (
        Product.objects
        .filter(is_active=True)
        .select_related("category")
        .order_by("-created_at")
    )[:8]

    context = {
        "categories": categories,
        "featured_products": featured_products,
        "latest_products": latest_products,
    }

    return render(
        request,
        "products/home.html",
        context
    )


def product_list(request):
    products = (
        Product.objects
        .filter(is_active=True)
        .select_related("category")
    )

    categories = Category.objects.all()

    search_query = request.GET.get("q", "").strip()
    category_slug = request.GET.get("category", "").strip()

    if search_query:
        products = products.filter(
            Q(name__icontains=search_query)
            | Q(description__icontains=search_query)
            | Q(short_description__icontains=search_query)
        )

    selected_category = None

    if category_slug:
        selected_category = get_object_or_404(
            Category,
            slug=category_slug
        )

        products = products.filter(
            category=selected_category
        )

    context = {
        "products": products,
        "categories": categories,
        "selected_category": selected_category,
        "search_query": search_query,
    }

    return render(
        request,
        "products/product_list.html",
        context
    )


def product_detail(request, slug):
    product = get_object_or_404(
        Product.objects.select_related("category"),
        slug=slug,
        is_active=True
    )

    related_products = (
        Product.objects
        .filter(
            category=product.category,
            is_active=True
        )
        .exclude(id=product.id)
        .select_related("category")
    )[:4]

    context = {
        "product": product,
        "related_products": related_products,
    }

    return render(
        request,
        "products/product_detail.html",
        context
    )


def category_products(request, slug):
    category = get_object_or_404(
        Category,
        slug=slug
    )

    products = (
        Product.objects
        .filter(
            category=category,
            is_active=True
        )
        .select_related("category")
    )

    categories = Category.objects.all()

    context = {
        "category": category,
        "products": products,
        "categories": categories,
    }

    return render(
        request,
        "products/product_list.html",
        context
    )