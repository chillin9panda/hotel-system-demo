# Generated by Django 5.1.3 on 2024-11-14 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_remove_employee_id_alter_employee_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(default='0000000000', max_length=20),
        ),
    ]
