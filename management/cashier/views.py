from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Create your views here.


def is_cashier(user):
    return user.role == 'Cashier'


@user_passes_test(is_cashier, login_url='/login/')
def cashier_main(request):
    return render(request, 'cashier/cashier_main.html')
