
from django.contrib import admin
from django.db import router
from django.urls import path

from home import views


urlpatterns = [
    path('goodsInfo/', views.BannerVeiwSet.as_view({'get': 'findBanners'})),
]

