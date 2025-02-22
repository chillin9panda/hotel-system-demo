from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

TRANSACTION_STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Successful', 'Successful'),
    ('Failed', 'Failed'),
]


PAYMENT_METHOD_CHOICES = [
    ('Cash', 'Cash'),
    ('Card', 'Card'),
    ('Mobile Banking', 'Mobile Banking'),
]


class Reception(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    service_payment_id = models.ForeignKey(
        'payments.Service_Payments', on_delete=models.CASCADE, null=True, related_name='service_payments')
    booking_payment_id = models.ForeignKey(
        'payments.Booking_Payments', on_delete=models.CASCADE, null=True, related_name='booking_payments')
    payed_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(
        max_length=15, choices=PAYMENT_METHOD_CHOICES)
    bank_name = models.CharField(max_length=50, null=True)
    transaction_date = models.DateTimeField(auto_now_add=True)
    transaction_status = models.CharField(
        max_length=15, choices=TRANSACTION_STATUS_CHOICES, default='Pending')

    def clean(self):
        if not self.service_payment_id and not self.booking_payment_id:
            raise ValidationError(
                "A transaction must be either linked to a service or booking.")

        if self.service_payment_id and self.booking_payment_id:
            raise ValidationError(
                "A transaction cannot be linked to a service and booking at once")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Transaction {self.transaction_id}"
