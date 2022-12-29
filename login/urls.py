
from django.contrib import admin
from django.db import router
from django.urls import path

from login import views


urlpatterns = [
    path('register/', views.RegisterVeiwSet.as_view({'post': 'userRegister'})),
    path('login/', views.LoginVeiwSet.as_view({'post': 'userLogin'})),
    path('add_address/', views.AddAddressVeiwSet.as_view({'post': 'userAddAddress'})),
    path('get_address/', views.AddAddressVeiwSet.as_view({'get': 'userGetAddress'})),
]

