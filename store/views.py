from django.shortcuts import render
from .models import *
# Create your views here.


def store(request):
    products = ProductMen.objects.all()
    productsWomen = ProductWomen.objects.all()
    productsKids = ProductKids.objects.all()

    context={'products':products, 'productsWomen':productsWomen, 'productsKids':productsKids}
    return render(request, 'store/store.html', context)

def cart(request):
    context={}
    return render(request, 'store/cart.html')

def checkout(request):
    context={}
    return render(request, 'store/checkout.html')


def view(request):
    context={}
    return render(request, 'store/view.html')