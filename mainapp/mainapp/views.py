from django.http import HttpResponse
from django.shortcuts import render




def home(request):
    products = ['Cherries', 'Apples', 'Pineapple', 'Strawberry', 'Peach']
    context = {
         #'user': user
        'products':products
    }
    return render(request, 'home.html', context)
