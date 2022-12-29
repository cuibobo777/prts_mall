
from django.contrib import admin
from django.db import router
from django.urls import path
from cart import views


urlpatterns = [
    path('to_cart/', views.CartVeiwSet.as_view({'post': 'addToCart'})),
    path('get_cart/', views.CartVeiwSet.as_view({'get': 'getCart'})),
    path('update_cart/', views.CartVeiwSet.as_view({'put': 'updateCart'})),
]

