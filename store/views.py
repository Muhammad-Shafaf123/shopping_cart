from django.shortcuts import render , redirect
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
import json
import datetime
from django.contrib import messages


from .models import *
from .forms import OrderForm, CreateUserForm




def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request, 'store/register.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('store')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
   
    return render(request, 'store/login.html', context)

def logoutUser(request):
    return redirect('login')

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    products = ProductMen.objects.all()
    productsWomen = ProductWomen.objects.all()
    productsKids = ProductKids.objects.all()

    context = {'products': products, 'productsWomen': productsWomen, 'productsKids': productsKids,
               'cartItems': cartItems}
    return render(request, 'store/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        artItems = order['get_cart_items']

    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)


def view(request):
    products = ProductMen.objects.all()
    productsWomen = ProductWomen.objects.all()
    productsKids = ProductKids.objects.all()

    context = {'products': products, 'productsWomen': productsWomen, 'productsKids': productsKids}
    return render(request, 'store/view.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = ProductMen.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    print('User in not logged in',request.body)
    return JsonResponse('Payment submitted..', safe=False)


	# # transaction_id = datetime.datetime.now().timestamp()
	# # data = json.loads(request.body)

	# # if request.user.is_authenticated:
	# # 	customer = request.user.customer
	# # 	order, created = Order.objects.get_or_create(customer=customer, complete=False)
    # #     total = data['form']['total']
    # #     order.transaction_id = transaction_id

    # #     if total == order.get_cart_total:
	# # 	    order.complete = True
	# #     order.save()

    # #     if order.shipping == True:
	# # 	ShippingAddress.objects.create(
	# # 	customer=customer,
	# # 	order=order,
	# # 	address=data['shipping']['address'],
	# # 	city=data['shipping']['city'],
	# # 	state=data['shipping']['state'],
	# # 	zipcode=data['shipping']['zipcode'],
	# # 	)


	# else:
   

