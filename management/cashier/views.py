from django.shortcuts import render

# Create your views here.


def cashier_main(request):
    return render(request, 'cashier/cashier_main.html')
