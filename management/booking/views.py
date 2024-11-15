from django.shortcuts import render, redirect
from .models import Room, Booking
from .forms import BookingForm

# Create your views here.


def booking_main(request):
    return render(request, 'booking/main.html')


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
