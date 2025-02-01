from django.db import models

# Create your models here.


class Booking_Payments(models.Model):
    PAYMENT_METHOD = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('Mobile Banking', 'Mobile Banking'),
    ]

    PAYMENT_STATUS = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Cancelled', 'Cancelled'),
    ]

    payment_id = models.AutoField(primary_key=True)
    booking_id = models.ForeignKey(
        'booking.Booking', on_delete=models.CASCADE, related_name='payments')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(
        max_length=20, choices=PAYMENT_METHOD, blank=True)
    bank_name = models.CharField(max_length=100, null=True, blank=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=15, choices=PAYMENT_STATUS, default='Pending')

    def __str__(self):
        return f"Payment {self.payment_id} for Booking {self.booking_id}"


class Service_Payments(models.Model):
    PAYMENT_METHOD = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('Mobile Banking', 'Mobile Banking'),
    ]

    PAYMENT_STATUS = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Cancelled', 'Cancelled'),
    ]

    service_payment_id = models.AutoField(primary_key=True)
    booking_id = models.ForeignKey(
        'booking.Booking', on_delete=models.CASCADE, related_name='service_payments')
    service_id = models.ForeignKey(
        'booking.services', on_delete=models.CASCADE, related_name='service')
    quantity = models.PositiveIntegerField(default=1)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(
        max_length=20, choices=PAYMENT_METHOD, blank=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=15, choices=PAYMENT_STATUS, default='Pending')

    def __str__(self):
        return self.service_payment_id
