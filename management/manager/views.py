from django.shortcuts import render, redirect
from django.http import JsonResponse

# Create your views here.
from booking.models import Room, Services
from django.contrib import messages


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
    return render(request, 'manager/manager_main.html')


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
    return render(request, 'manager/manager_main.html')


def manager_home(request):
    return render(request, 'manager/manager_main.html')
