from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import ValidationError
from .models import Room, Guest, Booking
from .forms import BookingForm
from django.http import JsonResponse
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.


def book_room(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        check_in_date = request.POST.get('check_in_date')
        check_out_date = request.POST.get('check_out_date')
        room_number = request.POST.get('room_number')

        # Get Room and Guest Objects
        try:
            room = Room.objects.get(room_number=room_number)

            guest, created = Guest.objects.get_or_create(
                phone_number=phone_number,
                defaults={'first_name': first_name,
                          'last_name': last_name,
                          'email': email,
                          }
            )

            # Booking instance
            booking = Booking(
                room=room,
                guest=guest,
                check_in_date=check_in_date,
                check_out_date=check_out_date,
            )

        # Validate and sabe booking
            try:
                booking.full_clean()
                booking.save()
                messages.success(request, "Booking Successfull")
                return redirect('booking_confirmation')
            except ValidationError as e:
                messages.error(request, f"Error: {e}")
                return redirect('booking_main')
        except Room.DoesNotExist:
            messages.error(request, "Room not Found!")
            return redirect('booking_main')
    else:
        available_rooms = Room.objects.filter(room_status='Available')
        return render(request, 'booking_main.html', {'rooms': available_rooms})

    return HttpResponse("Form Submitted")


def is_receptionist(user):
    return user.role == 'Receptionist'


@user_passes_test(is_receptionist, login_url='/login/')
def booking_main(request):
    return render(request, 'booking/booking_main.html')
