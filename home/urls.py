
from django.contrib import admin
from django.db import router
from django.urls import path

from home import views


urlpatterns = [
    path('banner/', views.BannerVeiwSet.as_view({'get': 'findBanners'})),
    path('grid/', views.GridVeiwSet.as_view({'get': 'findGrids'})),
]

