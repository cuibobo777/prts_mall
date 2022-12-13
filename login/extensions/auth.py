# -*- coding:utf-8 -*-
# @Time: 2022年12月12日 下午8:47
# @File: auth.py
# @Software: PyCharm
import jwt
from jwt import exceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings


class JwtHeaderAuthentication(BaseAuthentication):

    def authenticate(self, request):
        # 获取token并判断token的合法性
        user_token = request.META.get("HTTP_ACCESSTOKEN")
        salt = settings.SECRET_KEY
        # 1.对token进行切割
        # 2.解密第二段
        # 3.验证第三段

        try:
            payload = jwt.decode(user_token, salt, True)
        except exceptions.ExpiredSignatureError:
            raise AuthenticationFailed({'status': '500', 'message': 'token已失效', 'data': 'Error code 1002'})
        except jwt.DecodeError:
            raise AuthenticationFailed({'status': '500', 'message': 'token认证失败', 'data': 'Error code 1003'})
        except jwt.InvalidTokenError:
            raise AuthenticationFailed({'status': '500', 'message': '非法的token', 'data': 'Error code 1004'})

        return (payload, user_token)