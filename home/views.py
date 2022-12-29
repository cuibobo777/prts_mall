from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from rest_framework.decorators import action, authentication_classes

from home.models import Banner, Grid
from home.serializers import BannerSerializer, GridSerializer


class BannerVeiwSet(viewsets.ModelViewSet):
    """
    API Banner轮播图URL
    """
    serializer_class = BannerSerializer
    authentication_classes = []

    @action(methods=['GET'], detail=False, url_path='home/banner/')
    def findBanners(self, request):
        """
        获取banner图url
        :param request:
        """
        queryset = Banner.objects.values().filter(is_deleted=0)
        dataList = BannerSerializer(queryset, many=True)
        if queryset != '':
            return JsonResponse({'status': 200, 'data': dataList.data}, safe=False)
        else:
            return JsonResponse({'status': 500, 'data': '链接有误'})


class GridVeiwSet(viewsets.ModelViewSet):
    serializer_class = GridSerializer
    authentication_classes = []

    @action(methods=['GET'], detail=False, url_path='home/grid/')
    def findGrids(self, request):
        """
        获取banner图url
        :param request:
        """
        queryset = Grid.objects.values().order_by('grid_rank').filter(is_deleted=0)
        if queryset != '':
            return JsonResponse({'status': 200, 'data': list(queryset)}, safe=False)
        else:
            return JsonResponse({'status': 500, 'data': '链接有误'})
