# Generated by Django 5.1.3 on 2025-02-01 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_services'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookingPayments',
            new_name='Booking_Payments',
        ),
        migrations.RenameModel(
            old_name='ServicePayments',
            new_name='Service_Payments',
        ),
    ]
