from django.contrib.auth.models import User, Group
from rest_framework import serializers

from login.models import userAccount, userAddress


class UserAccountSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = userAccount
        fields = ['user_id', 'user_name', 'user_email']


class UserAddressSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = userAddress
        fields = ['address_id', 'user_id_id', 'consignee_name', 'consignee_name', 'consignee_phone',
                  'default_flag', 'province_name', 'city_name', 'region_name', 'detail_address',
                  'area_code']



