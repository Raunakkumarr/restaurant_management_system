from django import forms
from restaurant_management_app.models import menu_item, billing_detail

CHOICES = ['Hot Lemon Tea', 'Fanta']

class menuForm(forms.ModelForm):
   class Meta:
     model = menu_item
     fields = ('item_category', 'item_name', 'item_price')
     widgets = {
         'item_category':forms.TextInput(attrs={'class':'form-control'}),
         'item_name':forms.TextInput(attrs={'class':'form-control'}),
         'item_price':forms.TextInput(attrs={'class':'form-control'})
     }
