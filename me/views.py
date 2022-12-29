from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action

from me import models
from me.serializers import UserDetailInfoSerializer


class UserDetailInfoVeiwSet(viewsets.ModelViewSet):

    @action(methods=['GET'], detail=False, url_path='me/get_user_detail/')
    def userGetAddress(self, request):
        """
        比对数据库中的地址信息
        """
        user_id = request.GET.get('id')
        # print(request.GET)
        queryset = models.userDetailInfo.objects.filter(user_id_id=user_id)
        detailList = UserDetailInfoSerializer(queryset, many=True)
        # print(addressList.data)

        if detailList != '':
            return JsonResponse({'status': 200, 'message': "获取地址车列表成功", 'data': detailList.data}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '地址获取失败'})
