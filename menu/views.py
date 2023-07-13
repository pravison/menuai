from django.shortcuts import render , redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from . models import *
import datetime
import json
from .utils import cartData, guestOrder
from .forms import NewMenuForm, MenuCategoryForm, BestServedForm
from dashboard.models import Contacts, TableBooking, Gallery, Events, CustomerReview, Staff, Company, AboutUs, SocialMediaLink


# Create your views here.
def index(request):
    menus = Menu.objects.all()
    galleries = Gallery.objects.filter(featured=True)
    promotions = Menu.objects.filter(promotion=True)
    specials = Menu.objects.filter(special=True)
    events = Events.objects.all()
    reviews = CustomerReview.objects.filter(featured=True)
    staffs = Staff.objects.filter(featured=True)
    infos = Company.objects.all()#must correct this query to query the last updated
    abouts = AboutUs.objects.all()#must correct this query to query the last updated
    links = SocialMediaLink.objects.all()
    categorys = Category.objects.all()

    data = cartData(request)
    cartItems = data['cartItems']

    context = {
        'menus': menus,
        'promotions': promotions,
        'galleries':galleries,
        'specials': specials,
        'cartItems':cartItems,
        'events':events,
        'reviews':reviews,
        'infos':infos,
        'abouts': abouts,
        'staffs': staffs,
        'links':links,
        'categorys': categorys
    }
    return render(request, 'index.html', context)

@login_required
def customers(request):
    customers= Customer.objects.all()
    context={
        'customers':customers
    }
    return render(request, 'customers.html', context)

@login_required
def deleteCustomer(request, id):
    customer = get_object_or_404(Customer, id=id)
    customer.delete()
    return redirect(reverse('customers'))

@login_required
def menu(request):
    menus= Menu.objects.all()
    context={
        'menus':menus
    }
    return render(request, 'menu.html', context)

@login_required
def newMenu(request):
    if request.method == 'POST':
        form = NewMenuForm(request.POST , request.FILES)

        if form.is_valid():
            form.save()

            return redirect(reverse('menu'))
    else:
        form = NewMenuForm()
    context = {
        'form': form
    }
    return render(request, 'new_menu.html', context)

@login_required
def editMenu(request, id):
    if request.method == 'POST':
        menu= Menu.objects.get(id=id)
        form = NewMenuForm(request.POST, instance=menu)

        if form.is_valid():
            form.save
            return redirect(reverse('menu') )
    else:
        menu= Menu.objects.get(id=id)
        form = NewMenuForm(instance=menu)

    context= {
                'form': form,
                'success': True
            }
    return render(request, 'edit_menu.html', context)
    
@login_required
def delete(request, id):
    menu = get_object_or_404(Menu, id=id)
    menu.delete()
    return redirect(reverse('menu'))

def cart(request):
    infos = Company.objects.all()#must correct this query to query the last updated
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

        
    context = {
        'items': items,
        'order': order,
        'cartItems':cartItems,
        'infos':infos
    }
    return render (request, 'cart.html', context)

def checkout(request):
    infos = Company.objects.all()#must correct this query to query the last updated
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
        
    context = {
        'items': items,
        'order': order,
        'cartItems':cartItems,
        'infos':infos
    }
    return render(request, 'checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)

    menuId = data['menuId']
    action = data['action']

    print('menuId:' , menuId)
    print('action:' , action)

    customer = request.user.customer
    menu = Menu.objects.get(id=menuId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, menu=menu)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()


    return JsonResponse('item was added', safe= False)

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    TableInfo.objects.create(
        customer = customer,
        order = order,
        table_number =data['table']['number']
    )

    return JsonResponse('payment complete', safe= False)

def contactUs(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contacts(name=name, email=email, subject=subject, message=message,)

        contact.save()
        messages.success(request, 'Your request has been submitted, we will get back to you soon')
        return redirect('index')


def bookTable(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        people = request.POST['people']
        message = request.POST['message']

        booking = TableBooking(name=name, email=email, phone_number=phone, date=date, time=time, people=people, message=message,)

        booking.save()
        messages.success(request, 'Your table has been succesfully booked')
        return redirect('index')
    
@login_required
def addCategory(request):
    if request.method == 'POST':
        form = MenuCategoryForm(request.POST , request.FILES)

        if form.is_valid():
            form.save()

            return render(request, 'menu_category.html', {'success':True})
    else:
        form = MenuCategoryForm()
    context = {
        'form': form
    }
    return render(request, 'menu_category.html', context)

@login_required
def addBestTime(request):
    if request.method == 'POST':
        form = BestServedForm(request.POST , request.FILES)

        if form.is_valid():
            form.save()

            return render(request, 'best_time.html', {'success':True})
    else:
        form = BestServedForm()
    context = {
        'form': form
    }
    return render(request, 'best_time.html', context)
