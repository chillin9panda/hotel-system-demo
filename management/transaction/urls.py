from django.urls import path
from . import views

app_name = 'transaction'

urlpatterns = [
    path('reception/', views.process_payment, name='reception_payment'),
]
