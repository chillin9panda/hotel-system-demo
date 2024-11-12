from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.


def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect based on role
            if user.groups.filter(name='Receptionist').exists():
                return redirect('booking:booking_home')
            elif user.groups.filter(name='Stock_Manager').exists():
                return redirect('stock_managment:stock_home')
            else:
                return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "login/login.html")
