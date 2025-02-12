from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.


def login_view(request):
    DEAFAUT_PASSWORD = 'temp@123'

    if request.method == "POST":
        employee_id = request.POST.get("employee_id")
        password = request.POST.get("password")

        user = authenticate(
            request, employee_id=employee_id, password=password)

        if user is not None:
            print("Authorized: ", user)

            if password == DEAFAUT_PASSWORD:
                return render(request, 'login/new_login.html', {
                    'user': user,
                })

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


def new_login_view(request):
    User = get_user_model()

    if request.method == "POST":
        employee_id = request.POST.get("employee_id")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        user = User.objects.get(employee_id=employee_id)

        if new_password != confirm_password:
            return render(request, 'login/new_login.html', {
                'error_message': 'Passwords do not match',
                'user': user,
            })

        # user.password = make_password(new_password)
        user.set_password(new_password)

        user.save()

        return redirect('login:login')
    return redirect('login:login')


def logout_view(request):
    logout(request)
    return redirect('login:login')
