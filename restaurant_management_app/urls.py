from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import login_staff, change_password, menu, bill_amount

urlpatterns = [
    #path('', views.homepage, name="homepage"),
    path('', login_staff, name="logIn_staff"),
    path('admin/', admin.site.urls),
    path('change_password/', change_password, name="change-password"),
    path('menu/', menu, name="digital-menu"),
    path('bill/', bill_amount, name='bill-amount')
]
