from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.booking_main, name='home'),
    path('book_room/', views.book_room, name='book_room'),
    path('edit_booking/', views.edit_booking, name='edit_booking'),
    path('create_booking_view/', views.create_booking_view,
         name='create_booking_view'),
]
