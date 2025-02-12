from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import ValidationError
from .models import Room, Guest, Booking, Services
from payments.models import Booking_Payments, Service_Payments
from django.http import HttpResponse
from django.db import connection, transaction
from datetime import datetime
from django.utils import timezone

# Create your views here.

checked_in = "Checked-In"
checked_out = "Checked-Out"


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
            with transaction.atomic():

                # Create Booking
                booking = Booking(
                    room=room,
                    guest=guest,
                    check_in_date=check_in_date,
                    check_out_date=check_out_date,
                )

                booking.full_clean()
                booking.save()

                Booking_Payments.objects.create(
                    booking_id=booking,
                    total_amount=0,
                )

                room.room_status = 'Booked'
                room.save()

            messages.success(request, "Booking Successfull")
            return redirect('booking:home')

        except Room.DoesNotExist:
            messages.error(request, "Room not Found!")
            return redirect('booking:home')

        except ValidationError as e:
            messages.error(request, f"Error: {e}")
            return redirect('booking:home')

    return HttpResponse("Form Submitted")


def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id)
    available_rooms = Room.objects.filter(room_status='Available')

    old_room = booking.room

    if request.method == 'POST':
        check_in_str = request.POST.get('check_in_date')
        check_out_str = request.POST.get('check_out_date')
        new_room_number = request.POST.get('room_number')

        if check_out_str:
            check_out_date = datetime.strptime(
                check_out_str, "%Y-%m-%d").date()
            booking.check_out_date = check_out_date

        if check_in_str:
            check_in_date = datetime.strptime(check_in_str, "%Y-%m-%d").date()
            booking.check_in_date = check_in_date

        if new_room_number and new_room_number != old_room.room_number:
            new_room = get_object_or_404(Room, room_number=new_room_number)

            old_room.room_status = 'Available'
            old_room.save()

            new_room.room_status = 'Booked'
            new_room.save()

            booking.room = new_room

        booking.save()

        # update payment
        payment = Booking_Payments.objects.filter(booking_id=booking).first()

        if payment:
            check_in_date = booking.check_in_date
            check_out_date = booking.check_out_date

            if check_in_date and check_out_date:
                days_stayed = (check_out_date - check_in_date).days
                days_stayed = max(days_stayed, 1)
                room_price = booking.room.price
                total_amount = days_stayed * room_price

                payment.total_amount = total_amount
                payment.save()

        return redirect('booking:edit_booking', booking_id=booking_id)

    return render(request,
                  'booking/edit_booking.html', {
                      'booking': booking,
                      'available_rooms': available_rooms,
                  })


def room_service(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id)
    guest = booking.guest
    services = Services.objects.all()

    if request.method == 'POST':
        service_id = request.POST.get('service_id')
        quantity = int(request.POST.get('quantity', 1))

        service = get_object_or_404(Services, service_id=service_id)
        total_amount = service.service_price * quantity

        Service_Payments.objects.create(
            booking_id=booking,
            service_id=service,
            quantity=quantity,
            total_amount=total_amount,
            ordered_on=timezone.now(),
            payment_status='Unpaid',
        )

        messages.success(request, "Order Successfull!")
        return redirect('booking:room_service', booking_id=booking_id)

    used_services = Service_Payments.objects.filter(booking_id=booking_id)
    return render(request,
                  'booking/room_service.html', {
                      'booking': booking,
                      'guest_name': f"{guest.first_name} {guest.last_name}",
                      'room': booking.room,
                      'phone_number': guest.phone_number,
                      'services': services,
                      'used_services': used_services,
                  })


def view_payments(request, booking_id):
    service_payments = Service_Payments.objects.filter(booking_id=booking_id)
    booking_payments = Booking_Payments.objects.filter(booking_id=booking_id)

    bookings = Booking.objects.get(booking_id=booking_id)

    return render(request,
                  'booking/view_payments.html', {
                      'service_payments': service_payments,
                      'booking_payments': booking_payments,
                      'room_number': bookings.room,
                  })


def check_in(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id)

    if booking.status != checked_in:
        booking.status = checked_in
        booking.save()

    return redirect("booking:home")


def check_out(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id)

    payment_record = Booking_Payments.objects.filter(
        booking_id=booking_id).first()

    if not payment_record or payment_record.payment_status != "Paid":
        messages.error(
            request, "Check-Out cancelled. Pending Payments Found.", extra_tags="check_out")
        return redirect("booking:home")

    if booking.status == checked_in:
        booking.status = checked_out
        booking.save()

        if booking.room:
            booking.room.room_status = 'Available'
            booking.room.save()

    return redirect("booking:home")


def search_booking(request):
    phone_number = request.GET.get('phone_number', '')

    if phone_number:
        bookings = Booking.objects.filter(
            guest__phone_number=phone_number) if phone_number else None
    else:
        bookings = Booking.objects.all()
    return render(request,
                  'booking/booking_main.html', {
                      'bookings': bookings,
                      'search_query': phone_number,
                  })


def is_receptionist(user):
    return user.role == 'Receptionist'


@user_passes_test(is_receptionist, login_url='/login/')
def booking_main(request):
    all_rooms = Room.objects.all().order_by('room_number')
    available_rooms = Room.objects.filter(room_status='Available')
    booked_rooms = Room.objects.filter(room_status='Booked')

    total_rooms = all_rooms.count()
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
                      'all_rooms': all_rooms,
                      'available_rooms': available_rooms,
                      'booking_data': booking_data,
                  })


"""
DB Views Creation Section

    - To be moved later on to somewhere,
        it can be auto excutun when running the server
"""


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
