from django.contrib import admin

# Register your models here.
from goods.models import Goods


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['goods_id', 'goods_name', 'goods_intro', 'goods_category_id', 'goods_cover_img',
                    'goods_carousel', 'goods_detail_content', 'original_price', 'selling_price',
                    'stock_num', 'tag', 'goods_sell_status', 'goods_promotion_status', 'create_time']
    fieldsets = [
        ('商品名称', {'fields': ['goods_name']}),
        ('商品介绍', {'fields': ['goods_intro']}),
        ('商品分类ID', {'fields': ['goods_category_id']}),
        ('商品封面图片', {'fields': ['goods_cover_img']}),
        ('商品滚屏', {'fields': ['goods_carousel']}),
        ('商品详情内容', {'fields': ['goods_detail_content']}),
        ('原价', {'fields': ['original_price']}),
        ('售价', {'fields': ['selling_price']}),
        ('库存数量', {'fields': ['stock_num']}),
        ('标签', {'fields': ['tag']}),
        ('商品销售状态', {'fields': ['goods_sell_status']}),
        ('商品促销状态', {'fields': ['goods_promotion_status']}),
    ]
    list_per_page = 10


admin.site.register(Goods, GoodsAdmin)
# goods_id = models.AutoField(primary_key=True)  # 商品ID
# goods_name = models.CharField(max_length=100, null=True)  # 商品名称
# goods_intro = models.CharField(max_length=100, null=True)  # 商品介绍
# goods_category_id = models.IntegerField()  # 商品分类ID
# goods_cover_img = models.CharField(max_length=100, null=True)  # 商品封面图片
# goods_carousel = models.CharField(max_length=100, null=True)  # 商品滚屏
# goods_detail_content = models.CharField(max_length=100, null=True)  # 商品详情内容
# original_price = models.DecimalField(max_digits=19, decimal_places=2)  # 原价
# selling_price = models.DecimalField(max_digits=19, decimal_places=2)  # 售价
# stock_num = models.IntegerField(default=0, null=True)  # 库存数量
# tag = models.CharField(max_length=50)  # 标签
# goods_sell_status = models.IntegerField(default=0, null=True)  # 商品销售状态
# create_time = models.DateField(auto_now_add=True)