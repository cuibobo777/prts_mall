from django.contrib.auth.models import User, Group
from rest_framework import serializers

from home.models import Banner, Grid


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class BannerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Banner
        fields = ['carousel_id', 'carousel_url', 'redirect_url', 'carousel_rank']


class GridSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grid
        fields = ['grid_id', 'grid_url', 'redirect_url', 'grid_sort', 'grid_rank']