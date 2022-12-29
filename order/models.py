from django.db import models

# Create your models here.
from goods.models import Goods
from login.models import userAccount


class userOrder(models.Model):

    order_id = models.AutoField(primary_key=True)  # 订单信息ID
    order_no = models.IntegerField()  # 订单编码
    user_id = models.ForeignKey(userAccount, on_delete=models.CASCADE)  # 用户ID
    total_price = models.DecimalField(max_digits=19, decimal_places=2)  # 总价
    pay_status = models.IntegerField()   # 支付状态
    pay_type = models.IntegerField()   # 支付类型
    pay_time = models.DateField()     # 支付时间
    order_status = models.IntegerField()     # 订单状态
    extra_info = models.IntegerField(null=True, blank=True)  # 备注
    is_deleted = models.IntegerField(default=0)   # 是否删除
    create_time = models.DateField(auto_now_add=True)   # 创建时间

    class Meta:
        db_table = 'mall_order'


class userOrderItem(models.Model):

    order_item_id = models.AutoField(primary_key=True)  # 订单详细信息ID
    order_id = models.ForeignKey(userOrder, on_delete=models.CASCADE)  # 订单信息ID
    goods_id = models.ForeignKey(Goods, on_delete=models.CASCADE)  # 商品ID
    goods_name = models.CharField(max_length=100, null=True)   # 商品名称
    goods_cover_img = models.CharField(max_length=100, null=True)   # 商品封面图片
    selling_price = models.DecimalField(max_digits=19, decimal_places=2)   # 销售价格
    goods_count = models.IntegerField(default=0, null=True)     # 商品数量
    create_time = models.DateField(auto_now_add=True)   # 创建时间

    class Meta:
        db_table = 'mall_order_item'


class userOrderAddress(models.Model):

    order_address_id = models.AutoField(primary_key=True)  # 订单地址ID
    order_id = models.ForeignKey(userOrder, on_delete=models.CASCADE)  # 订单ID
    user_name = models.CharField(max_length=32)  # 收件人姓名
    user_phone = models.CharField(max_length=64)  # 收件人电话
    province_name = models.CharField(max_length=32)  # 省
    city_name = models.CharField(max_length=32)   # 市
    region_name = models.CharField(max_length=32)     # 区
    models.CharField(max_length=64)   # 详细地址

    class Meta:
        db_table = 'mall_order_address'



