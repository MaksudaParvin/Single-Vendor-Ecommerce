from django.db import models
from orders.models import Order


class Payment(models.Model):

    class Method(models.TextChoices):
        CASH_ON_DELIVERY = "cod", "Cash on Delivery"
        CARD = "card", "Card"
        MOBILE_BANKING = "mobile_banking", "Mobile Banking"

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        PAID = "paid", "Paid"
        FAILED = "failed", "Failed"

    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name="payment"
    )

    method = models.CharField(
        max_length=30,
        choices=Method.choices,
        default=Method.CASH_ON_DELIVERY
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    transaction_id = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    payment_date = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Payment - Order #{self.order.id}"