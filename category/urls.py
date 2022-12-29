
from django.contrib import admin
from django.db import router
from django.urls import path

from category import views

urlpatterns = [
    path('category/', views.CategoryVeiwSet.as_view({'get': 'findCategoryInfo'})),
]

