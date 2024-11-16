from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.booking_main, name='home'),
    path('book/', views.book_room, name='book_room'),
    path('success/', views.booking_success, name='booking_success'),
]
