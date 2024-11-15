from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from .models import Employee


class EmployeeIDBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **Kwargs):
        try:
            user = Employee.objects.get(employee_id=username)
        except Employee.DoesNotExist:
            user = None

        if not user:
            try:
                user = Employee.objects.get(phone_number=username)
            except Employee.DoesNotExist:
                user = None

        if user and user.check_password(password):
            return user
        return None
