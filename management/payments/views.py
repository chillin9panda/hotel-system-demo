from payments.models import Payments
from Booking.models import Booking
from django.Http import HttpResponse

# Create your views here.


def add_payment(request, booking_id):
    if request.method == "POST":
        booking_id = Booking.objects.get(id=booking_id)
        payment_method = request.POST.get('payment_method')
        amount = request.POST.get('amount')
        bank_name = request.POST.get('bank_name')
        transaction_id = request.POST.get('transaction_id')

    Payments.objects.create(
        booking_id=booking_id,
        payment_method=payment_method,
        amount=amount,
        bank_name=bank_name,
        transaction_id=transaction_id,
    )

    return HttpResponse(f"Payment added to Booking {booking_id}")
