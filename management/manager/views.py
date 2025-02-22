from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from booking.models import Room, Services
from login.models import Employee
from .forms import EmployeeForm
import csv
import datetime
from transaction.models import Reception
from django.utils.timezone import make_aware


# Create your views here.

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manager:home')
    else:
        form = EmployeeForm()

    return render(request,
                  'manager/add_employee.html', {
                      'form': form,
                  })


def add_room(request):
    if request.method == 'POST':
        room_number = request.POST.get('room_number')
        room_type = request.POST.get('room_type')
        price = request.POST.get('price')
        room_status = request.POST.get('room_status')

        # Add room to the database
        try:
            Room.objects.create(
                room_number=room_number,
                room_type=room_type,
                price=price,
                room_status=room_status
            )
            return JsonResponse({
                'success': True,
                'message': 'Room Added Successfully'})
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'Error{str(e)}'})
    return render(request, 'manager/add_room.html')


def add_service(request):
    if request.method == 'POST':
        service_name = request.POST.get('service_name')
        service_price = request.POST.get('service_price')

        # Add service to the database
        try:
            Services.objects.create(
                service_name=service_name,
                service_price=service_price,
            )
            return JsonResponse({
                'success': True,
                'message': 'Service Added Successfully'})
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'Error{str(e)}'})
    return render(request, 'manager/add_service.html')


def employee_details(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)
    return render(request, 'manager/employee.html', {
        'employee': employee,
    })


def generate_report(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    transactions = []
    if start_date and end_date:
        transactions = Reception.objects.filter(
            transaction_date__range=[start_date, end_date])

    return render(request, 'manager/manager_main.html', {
        'transactions': transactions,
        'start_date': start_date,
        'end_date': end_date,
    })


def export_report(request):
    start_date = make_aware(datetime.datetime.strptime(
        request.GET.get('start_date'), "%Y-%m-%d"))
    end_date = make_aware(datetime.datetime.strptime(
        request.GET.get('end_date'), "%Y-%m-%d"))

    transactions = Reception.objects.filter(
        transaction_date__range=[start_date, end_date])

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachement: filename="report_{
        start_date}_to_{end_date}.csv"'

    writer = csv.writer(response)
    writer.writerow(['No.', 'Payment Type', 'Amount',
                    'Date', 'Payment Method'])

    for index, transaction in enumerate(transactions, start=1):
        payment_type = transaction.service_payment_id.service_id.service_name if transaction.service_payment_id else transaction.booking_payment_id
        writer.writerow([index, payment_type, transaction.payed_amount,
                        transaction.transaction_date, transaction.payment_method])

    return response


def manager_home(request):
    active_employees = Employee.objects.filter(is_active=True)
    services = Services.objects.all()
    rooms = Room.objects.all()

    return render(request,
                  'manager/manager_main.html', {
                      'active_employees': active_employees,
                      'services': services,
                      'rooms': rooms,
                  })
