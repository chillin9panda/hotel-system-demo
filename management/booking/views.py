from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from .models import Room, Guest, Booking
from .forms import BookingForm
from django.http import JsonResponse

# Create your views here.


def book_room(request):
    if request.method == 'POST':
        guest_name = request.POST.get('guest_name')
        phone_number = request.POST.get('contact_number')
        check_in_date = request.POST.get('check_in_date')
        check_out_date = request.POST.get('check_out_date')
        room_number = request.POST.get('room_number')
        payment_method = request.POST.get('payment_method')
        bank_name = request.POST.get('bank_name')
        transaction_id = request.POST.get('transaction_id')

        # Get Room and Guest Objects
        try:
            room = Room.objects.get(room_number=room_number)
            guest, created = Guest.objects.get_or_create(
                phone_number=phone_number,
                default={'first_name': guest_name.split(
                )[0], 'last_name': ' '.join(guest_name.split()[1:])}
            )

            # Booking instance
            booking = Booking(
                room=room,
                guest=guest,
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                payment_method=payment_method,
                bank_name=bank_name if payment_method == 'Mobile Banking' else None,
                transaction_id=transaction_id if payment_method == 'Mobile Banking' else None
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


def is_receptionist(user):
    return user.role == 'Receptionist'


@user_passes_test(is_receptionist, login_url='/login/')
def booking_main(request):
    return render(request, 'booking/booking_main.html')
