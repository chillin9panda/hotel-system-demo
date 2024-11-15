from django.contrib import admin
from .models import Employee
# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'first_name', 'last_name',
                    'role', 'phone_number', 'date_joined')
    search_field = ('employee_id', 'first_name', 'last_name', 'role')
    list_filter = ('role', 'sex')


admin.site.register(Employee, EmployeeAdmin)
