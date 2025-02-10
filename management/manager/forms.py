from django import forms
from login.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'phone_number', 'sex', 'role']
        widgets = {
            'sex': forms.Select(choices=Employee.SEX_CHOICES),
            'role': forms.Select(choices=Employee.ROLE_CHOICES),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update(
            {'placeholder': 'Last Name'})
        self.fields['phone_number'].initial = None
        self.fields['phone_number'].widget.attrs.update(
            {'placeholder': 'Phone Number'})
