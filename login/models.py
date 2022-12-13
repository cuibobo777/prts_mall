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