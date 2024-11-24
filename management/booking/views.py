from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Room, Booking
from .forms import BookingForm

# Create your views here.


def is_receptionist(user):
    return user.role == 'Receptionist'


@user_passes_test(is_receptionist, login_url='/login/')
def booking_main(request):
    return render(request, 'booking/booking_main.html')
