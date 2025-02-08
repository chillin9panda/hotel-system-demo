from django.db import models
from datetime import timedelta

# Create your models here.


class Booking_Payments(models.Model):
    PAYMENT_METHOD = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('Mobile Banking', 'Mobile Banking'),
    ]

    PAYMENT_STATUS = [
        ('Unpaid', 'Unpaid'),
        ('Paid', 'Paid'),
        ('Cancelled', 'Cancelled'),
    ]

    payment_id = models.AutoField(primary_key=True)
    booking_id = models.ForeignKey(
        'booking.Booking', on_delete=models.CASCADE, related_name='payments')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bank_name = models.CharField(max_length=100, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=15, choices=PAYMENT_STATUS, default='Unpaid')

    def days_stayed(self):
        if self.booking_id.check_out_date and self.booking_id.check_in_date:
            return (self.booking_id.check_out_date - self.booking_id.check_in_date).days
        return 0

    def calculate_total_amount(self):
        days = self.days_stayed()
        room_price = self.booking_id.room.price if self.booking_id.room else 0
        return days*room_price

    def save(self, *args, **kwargs):
        self.total_amount = self.calculate_total_amount()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Payment {self.payment_id} for Booking {self.booking_id}"


class Service_Payments(models.Model):
    PAYMENT_METHOD = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('Mobile Banking', 'Mobile Banking'),
    ]

    PAYMENT_STATUS = [
        ('Unpaid', 'Unpaid'),
        ('Paid', 'Paid'),
        ('Cancelled', 'Cancelled'),
    ]

    payment_id = models.AutoField(primary_key=True)
    booking_id = models.ForeignKey(
        'booking.Booking', on_delete=models.CASCADE, related_name='service_payments')
    service_id = models.ForeignKey(
        'booking.services', on_delete=models.CASCADE, related_name='service')
    quantity = models.PositiveIntegerField(default=1)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_on = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=15, choices=PAYMENT_STATUS, default='Unpaid')

    def __str__(self):
        return self.service_payment_id
