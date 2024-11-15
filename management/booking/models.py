from django.db import models

# Create your models here.


class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.room_number}"


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return f"Booking for {self.guest_name} in Room {self.room.room_number}"
