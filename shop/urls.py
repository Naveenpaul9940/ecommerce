from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('collections/', collections, name='collections'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('checkout_success/', checkout_success, name='checkout_success'),
]
