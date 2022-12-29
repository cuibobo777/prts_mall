from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action

from goods.models import Goods
from goods.serializers import GoodsInfoSerializer


class GoodsVeiwSet(viewsets.ModelViewSet):
    """
    API 商品轮播图URL
    """
    authentication_classes = []
    serializer_class = GoodsInfoSerializer

    @action(methods=['GET'], detail=False, url_path='goods/goods/')
    def findGoodsInfo(self, request):
        """
        获取banner图url
        :param request:
        """
        queryset = Goods.objects.values().filter(goods_sell_status=0)
        if queryset != '':
            return JsonResponse({'status': 200, 'data': list(queryset)}, safe=False)
        else:
            return JsonResponse({'status': 500, 'data': '链接有误'})
