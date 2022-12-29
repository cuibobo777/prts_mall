from django.db import models

# Create your models here.
from goods.models import Goods
from login.models import userAccount


class Cart(models.Model):
    cart_item_id = models.AutoField(primary_key=True)   # 商品ID
    user_id = models.ForeignKey(userAccount, on_delete=models.CASCADE)  # userID
    goods_id = models.ForeignKey(Goods, on_delete=models.CASCADE)      # 商品ID
    goods_name = models.CharField(max_length=100, null=True)
    goods_cover_img = models.CharField(max_length=100, null=True)      # 商品封面图片
    selling_price = models.DecimalField(max_digits=19, decimal_places=2)        # 售价
    goods_count = models.IntegerField(default=0, null=True)      # 数量
    is_deleted = models.IntegerField(default=0)  # 是否删除
    create_time = models.DateField(auto_now_add=True)          # 创建时间

    class Meta:
        db_table = 'mall_cart'