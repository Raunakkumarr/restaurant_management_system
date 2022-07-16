import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from restaurant_management_app.forms import menuForm
from restaurant_management_app.models import menu_item, billing_detail, table_detail
from restaurant_management_app.functions import login_anywhere

# Create your views here.
def change_password(request):
    if request.method == 'POST':
        if 'username' in request.POST:
            login_anywhere(request)
        else:
            new_password = request.POST['new_password']
            re_new_password = request.POST['re_new_password']
            if new_password == re_new_password:
                old_password = request.POST['old_password']
                if User.check_password(request.user, old_password) == True:
                    User.set_password(request.user, new_password)
                    User.save(request.user)
                    messages.success(request, "Your Password Changed.")
                else:
                    messages.success(request, "Your old password did not match. Please try again...")
            else:
                messages.success(
                    request, "New Password and Retype New Password did not match. Please try again...")
        return redirect('/staff/change_password/')
    else:
        if request.user.is_authenticated:
            return redirect('/staff/')
        else:
            return render(request, 'staff/passwordChange.html', {})

def index_staff(request):
    if request.method == 'POST':
        login_anywhere(request)
        return redirect('/staff/')
    else:
        return render(request, 'staff/index.html', {})

def menu(request):
    if request.method == 'POST':
        if 'username' in request.POST:
            login_anywhere(request)
        else:
            form = menuForm(request.POST)
            if form.is_valid:
                form.save()
                messages.success(request, 'Item added successfully.')
        return redirect('/staff/menu/')
    else:
        modelForm = menuForm()
        items = menu_item.objects.all()
        if str(request.user.groups.filter(name='management')) == "<QuerySet [<Group: management>]>" or str(request.user.groups.filter(name='super-management')) == "<QuerySet [<Group: super-management>]>":
            context = {'group': 'has_group', 'form': modelForm, 'items':items}
        else:
            context = {'group': 'not_have_group', 'form': modelForm, 'items':items}
        return render(request, 'staff/menu.html', context)

def bill_amount(request):
    items = menu_item.objects.all()
    item_names_and_price = {}
    for i in items:
        item_names_and_price[i.item_name] = i.item_price
    if request.method == 'POST':
        if 'username' in request.POST:
            login_anywhere(request)
            return render(request, 'staff/print_bill.html', {'items': items})
        else:
            dateandtime = str(datetime.datetime.now())
            staffSigned = str(request.user.username)
            time = str(datetime.datetime.now().strftime("%H:%M:%S"))
            item_name = request.POST['items']
            price = item_names_and_price[item_name]
            quantity = request.POST['quantity']
            total_amount = int(price)*int(quantity)
            discount_p = request.POST['discount']
            tax_p = request.POST['tax']
            net_amount = int(total_amount)-(int(total_amount)*int(discount_p)/100)+((int(total_amount)-(int(total_amount)*int(discount_p)/100))*int(tax_p)/100)
            billing_detail.objects.create(dateandtime=dateandtime, signedBy=staffSigned, items=item_name, quantity=quantity, price=price, total_amount=total_amount, discount=discount_p, tax=tax_p, final_bill=net_amount)
            #messages.success(request, 'Bill Item was added to Database Successfully.')
            bill_calculated = {'item_name': item_name, 'item_price': price, 'item_quantity': quantity,
                            'amount': total_amount, 'discount': discount_p, 'tax': tax_p, 'net_bill': net_amount, 'date':datetime.date.today, 'time':time, 'staff':staffSigned}
            return render(request, 'staff/print_bill.html', {'items': items, 'bill':bill_calculated})
    else:
        return render(request, 'staff/print_bill.html', {'items':items})

def table_mgmt(request):
    if request.method == 'POST':
        if 'username' in request.POST:
            login_anywhere(request)
        elif 'New_table_status' in request.POST:
            last_table_no = int(table_detail.objects.last().table_no)
            table_detail.objects.create(dateandtime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), createdBy=request.user.username, table_no=last_table_no+1, table_status=request.POST['New_table_status'], table_status_checked_by=request.user.username)
            messages.success(request, 'New Table Record Added Successfully.')
        else:
            table_id = request.POST['table_id']
            messages.success(request, f'Status of Table No. {table_id} was changed from {table_detail.objects.get(table_no=table_id).table_status} to {request.POST["table_status_change"]}')
            table_detail.objects.filter(table_no=table_id).update(table_status=request.POST['table_status_change'])
        tables = table_detail.objects.all()
        if str(request.user.groups.filter(name='management')) == "<QuerySet [<Group: management>]>" or str(request.user.groups.filter(name='super-management')) == "<QuerySet [<Group: super-management>]>":
                context = {'group': 'has_group', 'tables': tables}
        else:
            context = {'tables': tables}
        return render(request, 'staff/table_mgmt.html', context)
    else:
        tables = table_detail.objects.all()
        if str(request.user.groups.filter(name='management')) == "<QuerySet [<Group: management>]>" or str(request.user.groups.filter(name='super-management')) == "<QuerySet [<Group: super-management>]>":
                context = {'group': 'has_group', 'tables': tables}
        else:
            context = {'tables':tables}
        return render(request, 'staff/table_mgmt.html', context)

def account_mgmt(request):
    context = {}
    if request.method == 'POST':
        if 'username' in request.POST:
            login_anywhere(request)
    else:
        if not request.user.is_authenticated:
            return redirect('/staff/')
    return render(request, 'staff/accounts.html', context)

def place_order(request):
    context = {}
    if request.method == 'POST':
        if 'username' in request.POST:
            login_anywhere(request)
    return render(request, 'staff/place_order.html', context)
