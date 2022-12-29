from django.contrib.auth.models import User, Group
from rest_framework import serializers

from me.models import userDetailInfo


class UserDetailInfoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = userDetailInfo
        fields = ['user_detail_id', 'user_id_id', 'nick_name', 'introduce', 'pic_url',
                  'PRTS_num', 'furniture_num', 'sex']




    # user_detail_id = models.AutoField(primary_key=True)  # 用户详细信息ID
    # user_id = models.ForeignKey(userAccount, on_delete=models.CASCADE)  # 用户ID
    # nick_name = models.CharField(max_length=32)  # 呢称
    # introduce = models.CharField(max_length=64, default="这个人很懒,什么也没有写")   # 个人简介
    # PRTS_num = models.IntegerField(max_length=32, default=500)   # PRTS积分
    # pic_url = models.CharField(max_length=100, default="default_head_portrait_from_prts.png")     # 头像连接
    # furniture_num = models.IntegerField(max_length=32, default=500)     # 家具币
    # is_deleted = models.IntegerField(default=0)   # 是否删除
    # create_time = models.DateField(auto_now_add=True)   # 创建时间