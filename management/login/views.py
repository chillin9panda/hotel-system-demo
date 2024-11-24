from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def login_view(request):
    if request.method == "POST":
        employee_id = request.POST.get("employee_id")
        password = request.POST.get("password")

        user = authenticate(
            request, employee_id=employee_id, password=password)

        if user is not None:
            print("Authorized: ", user)
        else:
            print("login attempt: ", employee_id)

        if user is not None:
            login(request, user)
            # Redirect based on role
            if user.role == 'Receptionist':
                return redirect('booking:home')
            elif user.role == 'System Admin':
                return redirect('admin:index')
            elif user.role == "Manager":
                return redirect('manager:home')
            else:
                return render(request, 'login/no_role.html')
        else:
            return render(request, 'login/login.html', {'error_message': 'Invalid Credentials'})
    return render(request, "login/login.html")


def logout_view(request):
    logout(request)
    return redirect('login:login')
