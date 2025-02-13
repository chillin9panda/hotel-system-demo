from django.urls import path
from . import views

app_name = 'cashier'

urlpatterns = [
    path('', views.cashier_main, name='home'),
]
