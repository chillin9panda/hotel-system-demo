from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.booking_main, name='home'),
    path('book_room/', views.book_room, name='book_room'),
    path('edit_booking/<int:booking_id>/',
         views.edit_booking, name='edit_booking'),
    path('room_service/<int:booking_id>/',
         views.room_service, name='room_service'),
    path('payments/<int:booking_id>/',
         views.view_payments, name='payments'),

    # Sql Views URL removed later
    path('create_booking_view/', views.create_booking_view,
         name='create_booking_view'),
]
