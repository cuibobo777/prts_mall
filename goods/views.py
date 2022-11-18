from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action

from goods.models import GoodsInfo


class GoodsInfoVeiwSet(viewsets.ModelViewSet):
    """
    API Banner轮播图URL
    """
    @action(methods=['GET'], detail=False, url_path='home/goodsInfo/')
    def findGoodsInfo(self, request):
        """
        获取banner图url
        :param request:
        """
        queryset = GoodsInfo.objects.values().filter(goods_sell_status=0)
        if queryset != '':
            return JsonResponse({'status': 200, 'data': list(queryset)}, safe=False)
        else:
            return JsonResponse({'status': 500, 'data': '链接有误'})
