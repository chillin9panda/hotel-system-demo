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


def book_room(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('booking:booking_success')
    else:
        form = BookingForm()
    return render(request, 'booking/book_room.html', {'form': form})


def booking_success(request):
    return render(request, 'booking/success.html')
