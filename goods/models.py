from django.db import models


# Create your models here.
from category.models import Category


class Goods(models.Model):
    goods_id = models.AutoField(primary_key=True)   # 商品ID
    goods_name = models.CharField(max_length=100, null=True)       # 商品名称
    goods_intro = models.CharField(max_length=100, null=True)      # 商品介绍
    goods_category_id = models.ForeignKey(Category, on_delete=models.CASCADE)       # 商品分类ID
    goods_cover_img = models.CharField(max_length=100, null=True)      # 商品封面图片
    goods_carousel = models.CharField(max_length=100, null=True)       # 商品滚屏
    goods_detail_content = models.CharField(max_length=100, null=True)     # 商品详情内容
    original_price = models.DecimalField(max_digits=19, decimal_places=2)       # 原价
    selling_price = models.DecimalField(max_digits=19, decimal_places=2)        # 售价
    stock_num = models.IntegerField(default=0, null=True)      # 库存数量
    tag = models.CharField(max_length=50)       # 标签
    goods_sell_status = models.IntegerField(default=0, null=True)       # 商品销售状态
    goods_promotion_status = models.IntegerField(default=0, null=True)
    create_time = models.DateField(auto_now_add=True)          # 创建时间

    class Meta:
        db_table = 'mall_goods'
