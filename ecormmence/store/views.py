from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth.models import User,auth
#from django.contrib import messages
from django.http import JsonResponse
from .models import *
# Create your views here.

def main(request):
    return render(request,'main.html')

def store(request):
    products = Product.objects.all()
    context ={
        'products':products
    }

    return render(request,'store.html',context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order ={'get_cart_total':0,'get_cart_items':0}
    context ={
       'items':items,'order': order
    }
    return render(request,'cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {
        'items': items, 'order': order
    }
    return render(request,'checkout.html')


def updateItem(request):
    return JsonResponse('item was added',safe=False)