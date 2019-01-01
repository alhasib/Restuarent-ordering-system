from django.shortcuts import render

from .models import *

def all_menu_items(request):
    all_items = MenuItem.objects.all()
    context = {'all_items':all_items}
    return render(request, 'all_menu.html', context)


def update_cart(request, item):
    print("hasib")
    print(item)
    return render(request, "cart.html", context)    

def cart_view(request):
    cart = Cart.objects.all()
    context = {'cart':cart}
    return render(request, 'cart.html', context)    