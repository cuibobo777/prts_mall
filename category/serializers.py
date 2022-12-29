from django.contrib.auth.models import User, Group
from rest_framework import serializers

from category.models import Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ['Category_id', 'Category_name', 'category_rank']