from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'guest', 'check_in_date', 'check_out_date',
                  'payment_method', 'bank_name', 'transaction_id']

        PAYMENT_CHOICE = [
            ('cash', 'cash'),
            ('card', 'card'),
            ('mobile banking', 'mobile banking'),
        ]

        payment_method = forms.ChoiceField(
            choices=PAYMENT_CHOICE, required=True)
        bank_name = forms.CharField(required=True)
        transaction_id = forms.CharField(required=True)

        def clean(self):
            cleaned_data = super().clean()
            payment_method = cleaned_data.get('payment_method')

            if payment_method == 'mobile-banking':
                if not cleaned_data('bank_name') or not cleaned_data.get('transaction_id'):
                    raise forms.ValidationError(
                        "Bank Name and Transaction Id are required for mobile banking payment.")
            return cleaned_data
