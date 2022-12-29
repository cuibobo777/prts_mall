from django.db import models

# Create your models here.


class userAccount(models.Model):

    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=32)
    user_password = models.CharField(max_length=64)
    user_token = models.CharField(max_length=64, null=True, blank=True)
    user_email = models.CharField(max_length=64, default="user@user.com")
    is_deleted = models.IntegerField(default=0)
    create_time = models.DateField(auto_now_add=True)  # 创建时间

    class Meta:
        db_table = 'userInfo'


class userAddress(models.Model):

    address_id = models.AutoField(primary_key=True)  # 地址 ID
    user_id = models.ForeignKey(userAccount, on_delete=models.CASCADE)  # 用户ID
    consignee_name = models.CharField(max_length=32)  # 收件人姓名
    consignee_phone = models.CharField(max_length=64)   # 收件人电话
    default_flag = models.IntegerField(default=0)   # 是否为默认地址
    province_name = models.CharField(max_length=32)     # 省
    city_name = models.CharField(max_length=32)     # 市
    region_name = models.CharField(max_length=32)   # 区
    area_code = models.IntegerField()  # 地区编码
    detail_address = models.CharField(max_length=64)    # 详细地址
    create_time = models.DateField(auto_now_add=True)   # 创建时间

    class Meta:
        db_table = 'userAddress'