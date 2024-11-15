from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'guest_name', 'check_in_date', 'check_out_date']
