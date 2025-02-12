from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseForbidden


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            if request.path not in ['/login/login/', '/login/new_login/']:
                return redirect(reverse('login:login'))

        if request.user.is_authenticated:
            # Booking
            if request.path.startswith('/booking/') and request.user.role != 'Receptionist':
                return HttpResponseForbidden("You are not authorized to view this page")

            if request.path.startswith('/manager/') and request.user.role != 'Manager':
                return HttpResponseForbidden("You are not authorized to view this page")

        response = self.get_response(request)
        return response
