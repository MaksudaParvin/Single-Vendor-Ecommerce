from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order",
        "method",
        "amount",
        "status",
        "transaction_id",
        "payment_date",
        "created_at",
    )

    list_filter = (
        "method",
        "status",
        "created_at",
    )

    search_fields = (
        "order__customer__name",
        "order__customer__phone",
        "transaction_id",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = ("-created_at",)