from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import index_staff, change_password, menu, bill_amount, table_mgmt, account_mgmt, place_order

urlpatterns = [
    path('', index_staff, name="logIn_staff"),
    path('admin/', admin.site.urls),
    path('change_password/', change_password, name="change-password"),
    path('menu/', menu, name="digital-menu"),
    path('bill/', bill_amount, name='bill-amount'),
    path('table/', table_mgmt, name='table-management'),
    path('accounts/', account_mgmt, name='accounts-manage'),
    path('orders/', place_order, name='place-order')
]
