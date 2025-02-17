from django.db import models

# Create your models here.


class Item(models.Model):
    ITEM_TYPE_CHOICES = [
        ('Food', 'Food'),
        ('Drinks', 'Drinks'),
    ]
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=30, null=False)
    item_type = models.CharField(
        max_length=15, choices=ITEM_TYPE_CHOICES, null=False)
    item_price = models.DecimalField(max_digits=8, decimal_places=2)
