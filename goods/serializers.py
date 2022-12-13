from django.contrib.auth.models import User, Group
from rest_framework import serializers

from goods.models import Goods


class GoodsInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goods
        fields = ['goods_name', 'goods_intro', 'goods_category_id',
                  'goods_cover_img', 'goods_carousel', 'goods_cover_img',
                  'goods_detail_content', 'original_price', 'selling_price', 'stock_num',
                  'tag'
                  ]