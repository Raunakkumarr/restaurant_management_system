from django.contrib import admin
from matplotlib.pyplot import cla
from restaurant_management_app.models import menu_item, billing_detail, table_detail, order

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


@admin.register(table_detail)
class tableStatus(admin.ModelAdmin):
	list_display = ('dateandtime', 'createdBy', 'table_no', 'table_status', 'table_status_checked_by')
	ordering = ['table_no', 'table_status',]
	search_fields = ('createdBy', 'table_no', 'table_status', 'table_status_checked_by')

@admin.register(order)
class orderItems(admin.ModelAdmin):
	list_display = ('dateandtime', 'createdBy', 'table_no', 'items', 'quantity', 'order_status', 'total_bill', 'paid_with')
	ordering = ['dateandtime','table_no']
	search_fields = ('dateandtime', 'createdBy', 'table_no', 'items', 'quantity', 'order_status', 'total_bill', 'paid_with')