
from django.contrib import admin
from django.db import router
from django.urls import path

from me import views

urlpatterns = [
    path('get_user_detail/', views.UserDetailInfoVeiwSet.as_view({'get': 'userGetAddress'})),
]

