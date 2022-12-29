from django.db import models

# Create your models here.


class Category(models.Model):
    Category_id = models.IntegerField(primary_key=True)   # 分类ID
    Category_name = models.CharField(max_length=100, null=True)       # 分类名称
    category_rank = models.IntegerField()       # 分类排名
    is_deleted = models.IntegerField()  # 是否删除
    create_time = models.DateField(auto_now_add=True)  # 创建时间

    class Meta:
        db_table = 'mall_category'