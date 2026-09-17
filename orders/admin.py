from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

    readonly_fields = (
        "product",
        "quantity",
        "price",
        "total_price",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer",
        "total_price",
        "status",
        "order_date",
    )

    list_filter = (
        "status",
        "order_date",
    )

    search_fields = (
        "customer__name",
        "customer__phone",
        "customer__email",
    )

    readonly_fields = (
        "order_date",
        "updated_at",
    )

    inlines = [
        OrderItemInline,
    ]

    ordering = ("-order_date",)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order",
        "product",
        "quantity",
        "price",
        "total_price",
    )

    search_fields = (
        "product__name",
        "order__customer__name",
    )

    list_filter = (
        "product",
    )