from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.


class EmployeeManager(BaseUserManager):
    def create_user(self, first_name, last_name, phone_number, sex, role, date_joined, password=None, **extra_fields):

        employee_id = Employee().generate_employee_id(first_name)
        user = self.model(
            # employee_id=employee_id,
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            role=role,
            date_joined=date_joined,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, phone_number, sex, role, password=None, **extra_fields):
        employee_id = Employee().generate_employee_id(first_name)

        user = self.model(
            # employee_id=employee_id,
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            role=role,
            **extra_fields,
        )

        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class Employee(AbstractBaseUser):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    ROLE_CHOICES = [
        ('System Admin', 'System Admin'),
        ('Manager', 'Manager'),
        ('Receptionist', 'Receptionist'),
        ('Stock Manager', 'Stock Manager'),
        ('Cashier', 'Cashier'),
        ('Security', 'Security'),
        ('Waiter', 'Waiter'),
        ('Waitress', 'Waitress'),
    ]

    username = models.CharField(max_length=50, blank=True, null=True)
    employee_id = models.CharField(primary_key=True,
                                   max_length=50, unique=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(
        unique=True, max_length=20, default='0000000000')
    sex = models.CharField(max_length=6, choices=SEX_CHOICES, default='M')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
    date_joined = models.DateTimeField(default=timezone.now)
    # username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = EmployeeManager()

    USERNAME_FIELD = 'employee_id'
    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'sex', 'role', 'phone_number', 'password']

    def generate_employee_id(self, first_name):
        from django.db.models import Max
        last_employee = Employee.objects.filter(
            first_name=first_name).aggregate(Max('employee_id'))
        max_id = last_employee.get('employee_id__max', 0)

        if max_id is None:
            max_id = 0

        next_id = max_id+1
        return f"{slugify(first_name)}{str(next_id).zfill(4)}"

    def has_perm(self, perm):
        return True

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.employee_id
        # auto set username to employee_id
        if not self.employee_id:
            self.employee_id = self.generate_employee_id(self.first_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"
