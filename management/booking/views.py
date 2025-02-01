from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import ValidationError
from .models import Room, Guest, Booking
from django.http import HttpResponse
from django.db import connection

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

            if room.room_status != 'Available':
                messages.error(request, "The selected room is not Available!")
                return redirect('booking_main')

            guest, created = Guest.objects.get_or_create(
                phone_number=phone_number,
                defaults={'first_name': first_name,
                          'last_name': last_name,
                          'email': email,
                          }
            )

            # Create Booking
            booking = Booking(
                room=room,
                guest=guest,
                check_in_date=check_in_date,
                check_out_date=check_out_date,
            )

            room.room_status = 'Booked'
            room.save()

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

    return HttpResponse("Form Submitted")


def create_booking_view(request):
    sql = """
        CREATE OR REPLACE VIEW booking_view AS
        SELECT
            b.booking_id,
            g.first_name,
            g.phone_number,
            r.room_number,
            b.status
        FROM booking_booking b
        JOIN booking_guest g ON b.guest_id = g.phone_number
        JOIN booking_room r ON b.room_id = r.room_number;
    """

    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
        return HttpResponse("View 'booking_view' created.")
    except Exception as e:
        return HttpResponse(f"Error creating view:  {str(e)}")


def is_receptionist(user):
    return user.role == 'Receptionist'


@user_passes_test(is_receptionist, login_url='/login/')
def booking_main(request):
    rooms = Room.objects.all()
    available_rooms = Room.objects.filter(room_status='Available')
    booked_rooms = Room.objects.filter(room_status='Booked')

    total_rooms = rooms.count()
    available_count = available_rooms.count()
    booked_count = booked_rooms.count()

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM booking_view;")
        booking_data = cursor.fetchall()

    return render(request,
                  'booking/booking_main.html',
                  {
                      'total_rooms': total_rooms,
                      'available_count': available_count,
                      'booked_count': booked_count,
                      'all_rooms': rooms,
                      'rooms': available_rooms,
                      'booking_data': booking_data,
                  })
