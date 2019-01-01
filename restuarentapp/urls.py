from django.urls import path
from .views import *
urlpatterns = [
    path('all_items', all_menu_items),
    path('update/cart/<item>', update_cart, name = 'update_cart'),
    path('cart', cart_view),
]
