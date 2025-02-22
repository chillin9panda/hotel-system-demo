from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path('', views.manager_home, name='home'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('add_room/', views.add_room, name="add_room"),
    path('add_service/', views.add_service, name='add_service'),
    path('employee/<str:employee_id>/', views.employee_details, name='employee'),
    path('generate_report/', views.generate_report, name='generate_report'),
    path('export_report/', views.export_report, name='export_report'),
]
