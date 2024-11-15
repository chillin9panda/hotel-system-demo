from django.contrib.auth.backends import BaseBackend
from .models import Employee


class EmployeeAuthenticationBackend(BaseBackend):
    def authenticate(self, request, employee_id=None, password=None):
        try:
            employee = Employee.objects.get(employee_id=employee_id)
            if employee.password == password:
                return employee
        except Employee.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Employee.objects.get(employee_id=user_id)
        except Employee.DoesNotExist:
            return None
