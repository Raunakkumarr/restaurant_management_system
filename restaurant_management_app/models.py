from statistics import mode
from django.db import models

# Create your models here.
class menu_item(models.Model):
    item_category = models.CharField('CATEGORY:', max_length=250)
    item_name = models.CharField('NAME:', max_length=250)
    item_price = models.CharField('PRICE:', max_length=250)

class billing_detail(models.Model):
    dateandtime = models.DateTimeField('Date and Time:', max_length=250)
    signedBy = models.CharField('Signed By:', max_length=250)
    items = models.CharField('Orders:', max_length=250)
    price = models.CharField('Price:', max_length=250)
    quantity = models.CharField('Quantity:', max_length=250)
    total_amount = models.CharField('Bill Amount:', max_length=25)
    discount = models.CharField('Discount:', max_length=250)
    tax = models.CharField('Tax:', max_length=250)
    final_bill = models.CharField('Net Amount:', max_length=250)