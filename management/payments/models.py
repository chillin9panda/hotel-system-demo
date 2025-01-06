from django.db import models

# Create your models here.


class Payments(models.Model):
    PAYMENT_METHOD_CHOICE = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('Mobile Banking', 'Mobile Banking'),
    ]

    payment_id = models.AutoField(primary_key=True)
    booking_id = models.ForeignKey(
        'booking.Booking', on_delete=models.CASCADE, related_name='payments')
    payment_method = models.CharField(
        max_length=20, choices=PAYMENT_METHOD_CHOICE, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bank_name = models.CharField(max_length=100, null=True, blank=True)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    isPaid = models.BooleanField(default=False)

    def __str__(self):
        return f"Paymen {self.payment_id} for Booking {self.booking_id}"
