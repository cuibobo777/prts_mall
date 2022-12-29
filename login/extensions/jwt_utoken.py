# -*- coding:utf-8 -*-
# @Time: 2022年12月12日 下午8:53
# @File: jwt_utoken.py
# @Software: PyCharm

import jwt
import datetime
from django.conf import settings


def create_token(payload, timeout=3):
    """
    用户登录后生成token
    """

    salt = settings.SECRET_KEY
    # 构造header
    headers = {
        'typ': 'jwt',
        'alg': 'HS256'
    }
    # 构造payload
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=timeout)
    token = jwt.encode(payload=payload, key=salt, algorithm='HS256', headers=headers).decode('utf-8')

    return token

