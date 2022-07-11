import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from restaurant_management_app.forms import menuForm
from restaurant_management_app.models import menu_item, billing_detail

# Create your views here.
def change_password(request):
    if request.method == 'POST':
        if 'username' in request.POST:
            user_name = request.POST['username']
            password = request.POST['password']
            user = authenticate(
                request=request, username=user_name, password=password)
            if user is not None:
                login(request, user)
                messages.success(
                    request, "You're successfully logged in...")
                return redirect('/staff/change_password/')
            else:
                messages.success(
                    request, "There was an error logging in, please try again...")
                return redirect('/staff/change_password/')
        else:
            new_password = request.POST['new_password']
            re_new_password = request.POST['re_new_password']
            if new_password == re_new_password:
                old_password = request.POST['old_password']
                if User.check_password(request.user, old_password) == True:
                    User.set_password(request.user, new_password)
                    User.save(request.user)
                    messages.success(request, "Your Password Changed.")
                    return redirect('/staff/change_password/')
                else:
                    messages.success(
                        request, "Your old password did not match. Please try again...")
                    return redirect('/staff/change_password/')
            else:
                messages.success(
                    request, "New Password and Retype New Password did not match. Please try again...")
                return redirect('/staff/change_password/')
    else:
        return render(request, 'staff/passwordChange.html', {})

def login_staff(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password =  request.POST['password']
        user = authenticate(request=request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            messages.success(
                request, "You're successfully logged in...")
            return redirect('/staff/')
        else:
            messages.success(request, "There was an error logging in, please try again...")
            return redirect('/staff/')
    else:
        return render(request, 'staff/index.html', {})

def menu(request):
    if request.method == 'POST':
        form = menuForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Item added successfully.')
        return redirect('/staff/menu/')
    else:
        if not request.user.is_authenticated:
            return redirect('/staff/')
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
        dateandtime = str(datetime.datetime.now())
        staffSigned = str(request.user.username)
        item_name = request.POST['items']
        price = item_names_and_price[item_name]
        quantity = request.POST['quantity']
        total_amount = int(price)*int(quantity)
        discount_p = request.POST['discount']
        tax_p = request.POST['tax']
        net_amount = int(total_amount)-(int(total_amount)*int(discount_p)/100)+((int(total_amount)-(int(total_amount)*int(discount_p)/100))*int(tax_p)/100)
        #billing_detail.objects.create(dateandtime=dateandtime, signedBy=staffSigned, items=item_name, quantity=quantity, price=price, total_amount=total_amount, discount=discount_p, tax=tax_p, final_bill=net_amount)
        messages.success(request, 'Bill Item was added to Database Successfully.')
        bill_calculated = {'item_name': item_name, 'item_price': price, 'item_quantity': quantity,
                           'amount': total_amount, 'discount': discount_p, 'tax': tax_p, 'net_bill': net_amount}
        return render(request, 'staff/print_bill.html', {'items': items, 'bill':bill_calculated})
    else:
        return render(request, 'staff/print_bill.html', {'items':items})
