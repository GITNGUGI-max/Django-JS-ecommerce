import json
from .models import *


def cookieCart(request):
    try:
        cart= json.loads(request.COOKIES['cart'])  
    except:
        cart ={}
        print('cart:', cart)
    items =[]
    order = {'get_cart_items':0, 'get_cart_total':0}
    cartItems = order['get_cart_items']

    for i in cart:
        try:
            if(cart[i]['quantity']>0):
                cartItems += cart[i]['quantity']

                product = MenuItems.objects.get(id=i)

                total = (product.price* cart[i]['quantity'])

                order['get_cart_items'] += cart[i]['quantity']
                order['get_cart_total'] += total

                item = {
                    'product':{
                        'id':product.id,
                        'name':product.name,
                        'price':product.price,
                        'imageURL':product.imageURL,
                    },
                    'quantity':cart[i]['quantity'],
                    'get_total':total,
                }
                items.append(item)
        except:
                pass
    return {'items':items, 'order':order, 'cartItems':cartItems}

def cartData(request):
     
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
     
    return {'items':items, 'order':order, 'cartItems':cartItems}

def guestOrder(request, data):

    print('User is not logged in ...')

    print('Cookies', request.COOKIES)

    name = data['form']['name']
    email = data['form']['email']

    cookieData = cookieCart(request)
    items = cookieCart['items']

    customer, created = Customer.objects.get_or_create(email=email)
    customer.name = name
    customer.save()

    order = Order.objects.create(
            customer=customer,
            complete=False
        )

    for item in items:

            product = MenuItems.objects.get(id=item['product']['id'])

            orderItem = OrderItem.objects.create(
                product=product,
                order=order,
                quantity=(item['quantity'] if item['quantity']>0 else -1*item['quantity']),
            )

    return customer, data