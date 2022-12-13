
from django.contrib import admin
from django.db import router
from django.urls import path
from goods import views


urlpatterns = [
    path('goods/', views.GoodsVeiwSet.as_view({'get': 'findGoodsInfo'})),
]

