import json

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from school.models import *
from django.http import HttpResponseRedirect
from django.http import JsonResponse
#Comments
# from school.serializers import CommentsSerializer


# Create your views here.


def Store(request):
    products = Product.objects.all()
    order, create = Order.objects.get_or_create()
    cartItems = order.cart_quantity
    context = {
        'products': products,
        'cartItems' : cartItems
    }
    return render(request, 'store.html', context)


def cart(request):
    order, create = Order.objects.get_or_create()
    items = order.orderitem_set.all()
    cartItems = order.cart_quantity
    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems
    }
    return render(request, 'cart.html', context)

def checkout(request):
    order, created = Order.objects.get_or_create()
    items = order.orderitem_set.all()
    cartItems = order.cart_quantity
    context = {'items': items,
               'order': order,
               'cartItems': cartItems
               }
    return render(request, 'checkout.html', context)

def updateItem(request):
    #parse data throught json that we sent we json via javascript
    #we catch this data because we sent it to our url related to this view
        data = json.loads(request.body)
        #get productId
        productId = data['productId']
        action = data['action']
        print('Action', action)
        print('productId', productId)

        product = Product.objects.get(id=productId)
        order, create = Order.objects.get_or_create()
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)
        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)

        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()

        return JsonResponse({'message': 'Item updated successfully'})



# def updateItem(request):
#     data = json.loads(request.body)
#     productId = data['productId']
#     action = data['action']
#     print('Action:', action)
#     print('Product ID:', productId)
#
#     product = Product.objects.get(id=productId)
#     order, created = Order.objects.get_or_create(completed=False)
#
#     try:
#         orderItem = OrderItem.objects.filter(order=order, product=product).first()
#         print('Existing OrderItem:', orderItem)
#     except ObjectDoesNotExist:
#         orderItem = OrderItem(order=order, product=product)
#         print('New OrderItem:', orderItem)
#
#     if action == 'add':
#         orderItem.quantity += 1
#     elif action == 'remove':
#         orderItem.quantity -= 1
#
#     if orderItem.quantity <= 0:
#         orderItem.delete()
#         print('OrderItem deleted')
#     else:
#         orderItem.save()
#         print('OrderItem saved')
#
#     return JsonResponse({'message': 'Item updated successfully'})



# class CommentsViewSet(ModelViewSet):
#     queryset = Comments.objects.all()
#     serializer_class = CommentsSerializer
    #get all objects of current source
    # def list(self, request):
    #     return Response({'status':'OK'})
    #
    # # to let viewset look at specific object
    # def retrive(self, request):
    #     pass
    #
    # #delete
    # def destroy(self,request):
    #     pass
    #
    # #update
    # def update(self, request):
    #     pass
    #
    # def create(self, request):
    #     pass