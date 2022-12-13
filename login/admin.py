from django.contrib import admin

# Register your models here.
from login.models import userAccount


class LoginAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_email', 'create_time']

    fieldsets = [
        ('用户名', {'fields': ['user_name']}),
        ('用户邮箱', {'fields': ['user_email']}),
        ('创建时间', {'fields': ['create_time']}),
    ]

    list_per_page = 10


admin.site.register(userAccount, LoginAdmin)