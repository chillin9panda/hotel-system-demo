from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    # path('admin/', custom_admin_site.urls),
    # path('admin/login/', LoginView.as_view(template_name='custom_admin/admin_login.html'), name='admin-login'),
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('booking/', include('booking.urls')),
    path('manager/', include('manager.urls')),
    path('', lambda request: redirect('login')),
]
