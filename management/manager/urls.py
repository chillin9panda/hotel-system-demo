from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path('', views.manager_home, name='home'),
    path('add_room', views.add_room, name="add_room"),
]
