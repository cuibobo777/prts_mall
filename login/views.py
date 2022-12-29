import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action

from login import models
from login.extensions.jwt_utoken import create_token
from login.models import userAccount
from me.models import userDetailInfo
from login.serializers import UserAccountSerializer, UserAddressSerializer


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
        userData = json.loads(request.body.decode('utf-8'))
        username = userData.get("username")
        password = userData.get("password")
        userEmail = userData.get("email")
        newUser = userAccount(user_name=username, user_password=password, user_email=userEmail)
        newUser.save()
        # newUserId = models.userAccount.objects.filter(user_id=newUser.user_id).first()
        nick_name = "用户" + str(newUser.user_id)
        res = userDetailInfo.objects.create(nick_name=nick_name, user_id_id=newUser.user_id)
        # res = models.userAccount.objects.create(user_name=username, user_password=password, user_email=userEmail)
        if newUser.user_id != '' and res != '':
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
        # user_obj = models.userAccount.objects.filter(user_name=uname, user_password=pwd)
        # res = UserAccountSerializer(user_obj,many=True)
        # print(res.data)
        if user_obj:
            token = create_token({'id': user_obj.user_id, 'name': user_obj.user_name}, timeout=60)
            return JsonResponse({'status': 200, 'message': "账户登录成功", 'data': token, 'user_id': user_obj.user_id}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '用户名或密码错误', 'code': '1001'})
        # return HttpResponse('xunxingchengong')


class AddAddressVeiwSet(viewsets.ModelViewSet):
    """
    API 用户账号注册
    """

    authentication_classes = []

    @action(methods=['POST'], detail=False, url_path='login/add_address/')
    def userAddAddress(self, request):
        """
        将用户信息持久化
        """
        addressData = json.loads(request.body.decode('utf-8'))
        print(addressData)
        user_id = addressData.get("user_id")
        consignee_name = addressData.get("name")
        consignee_phone = addressData.get("tel")
        default_flag = addressData.get("isDefault")
        province_name = addressData.get("province")
        city_name = addressData.get("city")
        region_name = addressData.get("county")
        area_code = addressData.get("areaCode")
        detail_address = addressData.get("addressDetail")
        address_id = addressData.get("address_id")

        if default_flag:
            default_flag = 1
        else:
            default_flag = 0

        if address_id:
            print(default_flag)
            print(user_id)
            if default_flag == 1:
                res2 = models.userAddress.objects.filter(user_id_id=user_id).update(default_flag=0)
                print(res2)
                res = models.userAddress.objects.filter(address_id=address_id).update(
                    consignee_name=consignee_name,
                    consignee_phone=consignee_phone,
                    default_flag=default_flag,
                    province_name=province_name,
                    city_name=city_name,
                    region_name=region_name,
                    area_code=area_code,
                    detail_address=detail_address,
                )
            else:
                res = models.userAddress.objects.filter(address_id=address_id).update(
                    consignee_name=consignee_name,
                    consignee_phone=consignee_phone,
                    default_flag=default_flag,
                    province_name=province_name,
                    city_name=city_name,
                    region_name=region_name,
                    area_code=area_code,
                    detail_address=detail_address,
                )
        else:
            if default_flag == 1:
                res2 = models.userAddress.objects.filter(user_id_id=user_id).update(default_flag=0)
                res = models.userAddress.objects.create(
                    user_id_id=user_id,
                    consignee_name=consignee_name,
                    consignee_phone=consignee_phone,
                    default_flag=default_flag,
                    province_name=province_name,
                    city_name=city_name,
                    region_name=region_name,
                    area_code=area_code,
                    detail_address=detail_address,
                )
            else:
                res = models.userAddress.objects.create(
                    user_id_id=user_id,
                    consignee_name=consignee_name,
                    consignee_phone=consignee_phone,
                    default_flag=default_flag,
                    province_name=province_name,
                    city_name=city_name,
                    region_name=region_name,
                    area_code=area_code,
                    detail_address=detail_address,
                )
        if res != '':
            return JsonResponse({'status': 200, 'message': "地址添加成功"}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '地址添加失败'})

    @action(methods=['GET'], detail=False, url_path='login/get_address/')
    def userGetAddress(self, request):
        """
        比对数据库中的地址信息
        """
        user_id = request.GET.get('id')
        # print(request.GET)
        orderAddressId = request.GET.get("address_id")
        addressIsDefault = request.GET.get("isdefault")
        if user_id:
            queryset = models.userAddress.objects.filter(user_id_id=user_id)
        elif orderAddressId == '0':
            queryset = models.userAddress.objects.filter(default_flag=1)
        else:
            queryset = models.userAddress.objects.filter(address_id=orderAddressId)
        addressList = UserAddressSerializer(queryset, many=True)
        # print(addressList.data)

        if addressList != '':
            return JsonResponse({'status': 200, 'message': "获取地址车列表成功", 'data': addressList.data}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '地址获取失败'})

