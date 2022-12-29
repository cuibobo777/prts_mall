"""prts_mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home import views as homeViews
from goods import views as goodsViews
from login import views as loginViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('goods/', include('goods.urls')),
    path('login/', include('login.urls')),
    path('category/', include('category.urls')),
    path('cart/', include('cart.urls')),
    path('me/', include('me.urls')),
]

router = DefaultRouter()
router.register(r'home/banner', homeViews.BannerVeiwSet, basename='banner')
router.register(r'goods/goods', goodsViews.GoodsVeiwSet, basename='goods')
urlpatterns += router.urls

