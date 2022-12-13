from django.contrib.auth.models import User, Group
from rest_framework import serializers

from login.models import userAccount


class UserAccountSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = userAccount
        fields = ['user_name', 'user_email', 'create_time']