from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action

from category.models import Category
from category.serializers import CategorySerializer


class CategoryVeiwSet(viewsets.ModelViewSet):
    """
    API 分类
    """
    authentication_classes = []

    @action(methods=['GET'], detail=False, url_path='category/category/')
    def findCategoryInfo(self, request):
        """
        获取分类信息
        :param request:
        """
        queryset = Category.objects.values().filter(is_deleted=0).order_by('-category_rank')
        category_list = CategorySerializer(queryset, many=True)
        if queryset != '':
            # return JsonResponse({'status': 200, 'data': list(queryset)}, safe=False)
            return JsonResponse({'status': 200, 'data': category_list.data}, safe=False)
        else:
            return JsonResponse({'status': 500, 'data': '链接有误'})