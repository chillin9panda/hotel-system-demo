from django.db import models
import datetime

# Create your models here.


class Room(models.Model):
    ROOM_TYPE_CHOICES = [
        ('Single', 'Single'),
        ('Double', 'Double'),
    ]

    ROOM_STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Booked', 'Booked'),
        ('Maintenance', 'Maintenance'),
    ]

    room_number = models.CharField(max_length=10, primary_key=True)
    room_type = models.CharField(
        max_length=20, choices=ROOM_TYPE_CHOICES, default='Single')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    room_status = models.CharField(
        max_length=15, choices=ROOM_STATUS_CHOICES, default='Available')

    def __str__(self):
        return self.room_number

    class Meta:
        ordering = ['room_number']  # sort by room number


class Guest(models.Model):
    phone_number = models.CharField(max_length=15, primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone_number}"

    class Meta:
        ordering = ['first_name']  # sort by first name


class Booking(models.Model):
    BOOKING_STATUS_CHOICES = [
        ('Confirmed', 'Confirmed'),
        ('Pending', 'Pending'),
        ('Cancelled', 'Cancelled'),
    ]
    booking_id = models.AutoField(primary_key=True)
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name='bookings')
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, null=True,
                              related_name='bookings')
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    booking_date = models.DateTimeField(default=datetime.datetime.now)
    status = models.CharField(
        max_length=10, choices=BOOKING_STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Booking {self.booking_id}: for {self.guest.first_name} {
            self.guest.last_name}: in Room {self.room.room_number}"


class Services(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=50, unique=True)
    service_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.service_name
