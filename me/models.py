from django.db import models

# Create your models here.
from login.models import userAccount


class userDetailInfo(models.Model):

    user_detail_id = models.AutoField(primary_key=True)  # 用户详细信息ID
    user_id = models.ForeignKey(userAccount, on_delete=models.CASCADE)  # 用户ID
    nick_name = models.CharField(max_length=32)  # 呢称
    sex = models.CharField(max_length=16, default="保密")
    introduce = models.CharField(max_length=64, default="这个人很懒,什么也没有写")   # 个人简介
    PRTS_num = models.IntegerField(default=500)   # PRTS积分
    pic_url = models.CharField(max_length=100, default="default_head_portrait_from_prts.png")     # 头像连接
    furniture_num = models.IntegerField(default=500)     # 家具币
    is_deleted = models.IntegerField(default=0)   # 是否删除
    create_time = models.DateField(auto_now_add=True)   # 创建时间

    class Meta:
        db_table = 'userdetail'