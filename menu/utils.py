import json
from .models import *

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    print('cart:' , cart)
    items =[]
    order = {
        'get_cart_total':0 , 'get_cart_items':0
    }
    cartItems = order['get_cart_items']

    for i in cart:
        try:
            cartItems += cart[i]['quantity']

            menu = Menu.objects.get(id=i)
            total = (menu.price * cart[i]['quantity'])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']

            item = {
                'menu': {
                    'id': menu.id,
                    'name':menu.name,
                    'price': menu.price,
                    'imageURL': menu.imageURL,
                    },
                'quantity': cart[i]['quantity'],
                'get_total': total
                }
            items.append(item)
        except:
            pass
    return { 'items': items, 'order': order, 'cartItems':cartItems }

def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items= order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        items = cookieData['items']
        order = cookieData['order']
    return{ 'items': items, 'order': order, 'cartItems':cartItems }


def guestOrder(request , data):
    print('user is not logged in')

    print('COOKIES:', request.COOKIES)
    name = data['form']['name']
    email = data['form']['email']

    cookieData = cookieCart(request)
    items = cookieData['items']

    customer = Customer.objects.create(
        email=email,
        name =name,
    )
    

    order = Order.objects.create(
        customer=customer,
        complete=False
    )

    for item in items:
        menu = Menu.objects.get(id=item['menu']['id'])

        orderItem = OrderItem.objects.create(
            menu=menu,
            order = order,
            quantity = item['quantity']
        )
    return customer , order

        