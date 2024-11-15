from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    employer_id = forms.CharField(label='username', max_length=100)

    def clean_employer_id(self):
        employer_id = self.clean_data.get('employer_id')
        return employer_id
