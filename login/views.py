import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action

from login import models
from login.extensions.jwt_utoken import create_token
from login.models import userAccount
from login.serializers import UserAccountSerializer


class RegisterVeiwSet(viewsets.ModelViewSet):
    """
    API 用户账号注册
    """
    queryset = userAccount.objects.all().order_by('user_id')
    serializer_class = UserAccountSerializer
    authentication_classes = []

    @action(methods=['POST'], detail=False, url_path='login/register/')
    def userRegister(self, request):
        """
        将用户信息持久化
        """
        username = request.POST.get("username")
        password = request.POST.get("password")
        userEmail = request.POST.get("userEmail")
        res = models.userAccount.objects.create(user_name=username, user_password=password, user_email=userEmail)
        if res != '':
            return JsonResponse({'status': 200, 'message': "账户注册成功"}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '注册失败'})


class LoginVeiwSet(viewsets.ModelViewSet):
    """
    API 用户登录
    """
    authentication_classes = []

    @action(methods=['POST'], detail=False, url_path='login/login/')
    def userLogin(self, request):
        """
        比对数据库中的用户信息
        """
        userData = json.loads(request.body.decode('utf-8'))
        # print(userData)
        uname = userData.get("username")
        pwd = userData.get("password")
        # print(uname, pwd)
        user_obj = models.userAccount.objects.filter(user_name=uname, user_password=pwd).first()
        # print(user_obj)
        if user_obj:
            token = create_token({'id': user_obj.user_id, 'name': user_obj.user_name}, timeout=10)
            return JsonResponse({'status': 200, 'message': "账户登录成功", 'data': token}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '用户名或密码错误', 'data': 'Error code: 1001'})