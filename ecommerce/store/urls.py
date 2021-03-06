from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static
app_name = 'store'
urlpatterns = [
    path('', store, name='store'),
    path('cart/add/<int:id>/', cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         item_increment, name='item_increment'),
    path('cart/cart_clear/', cart_clear, name='cart_clear'),
    path('cart/cart_detail/', cart_detail, name='cart_detail'),
]