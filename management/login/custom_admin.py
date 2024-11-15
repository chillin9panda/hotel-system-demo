from django.contrib.admin import AdminSite
from django.contrib import admin


class CustomAdminSite(AdminSite):
    site_header = "My Custom Admin"
    site_title = "Admin Portal"
    index_title = "Welcome to Admin Portal"
    login_template = 'custom_admin/admin_login.html'


custom_admin_site = CustomAdminSite(name='my_custom_admin')
