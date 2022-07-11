from django.contrib import admin
from restaurant_management_app.models import menu_item, billing_detail

# Register your models here.
#admin.site.register(menu_items)


@admin.register(menu_item)
class menuItems(admin.ModelAdmin):
	list_display = ('item_category', 'item_name', 'item_price')
	ordering = ('item_category', 'item_price',)
	search_fields = ('item_name', 'item_price')


@admin.register(billing_detail)
class billItems(admin.ModelAdmin):
	list_display = ('dateandtime', 'signedBy', 'items', 'price', 'quantity', 'total_amount', 'discount', 'tax', 'final_bill')
	ordering = ['dateandtime',]
	search_fields = ('dateandtime', 'signedBy', 'items', 'price', 'total_amount',
	                 'discount', 'tax', 'final_bill')
