from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from payments.models import Booking_Payments, Service_Payments
from booking.models import Booking
from .models import Reception

# Create your views here.


def process_payment(request):
    checked_in = "Checked-In"

    if request.method == "POST":
        payment_type = request.POST.get("payment_type")
        payment_id = request.POST.get("payment_id")
        payment_method = request.POST.get("payment_method")
        payed_amount = request.POST.get("payed_amount")
        bank_name = request.POST.get("bank_name")

        if payment_type == "Booking":
            payment_record = get_object_or_404(
                Booking_Payments, payment_id=payment_id)

            booking = get_object_or_404(
                Booking, booking_id=payment_record.booking_id_id)
        elif payment_type == "Service":
            payment_record = get_object_or_404(
                Service_Payments, payment_id=payment_id)

            booking = None
        else:
            return JsonResponse({"error": "Invalid payment type"}, status=400)

        transaction = Reception(
            booking_payment_id=payment_record if payment_type == "Booking" else None,
            service_payment_id=payment_record if payment_type == "Service" else None,
            payed_amount=payed_amount,
            payment_method=payment_method,
            bank_name=bank_name,
            transaction_status="Successful",
        )

        transaction.save()

        payment_record.payment_status = "Paid"
        payment_record.save()

        if booking and booking.status != checked_in:
            booking.status = checked_in
            booking.save()

        return redirect(request.META.get("HTTP_REFERER", "booking:payments"))
    return JsonResponse({"error": "Invalid request"}, status=400)
