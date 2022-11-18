from django.contrib import admin

# Register your models here.
from home.models import Banner, Grid

admin.AdminSite.site_header = "PRTS管理系统"
admin.AdminSite.site_title = "PRTS管理系统"


class BannerAdmin(admin.ModelAdmin):
    list_display = ['carousel_id', 'carousel_url', 'redirect_url', 'carousel_rank', 'is_deleted', 'create_time']
    fieldsets = [
        ('轮播图URL', {'fields': ['carousel_url']}),
        ('链接地址', {'fields': ['redirect_url']}),
        ('轮播顺序', {'fields': ['carousel_rank']}),
        ('是否删除', {'fields': ['is_deleted']}),
    ]
    list_per_page = 10

class GridAdmin(admin.ModelAdmin):
    list_display = ['grid_id', 'grid_url', 'grid_sort', 'redirect_url', 'grid_rank', 'is_deleted', 'create_time']
    fieldsets = [
        ('宫格图URL', {'fields': ['grid_url']}),
        ('链接地址', {'fields': ['redirect_url']}),
        ('图片分类', {'fields': ['grid_sort']}),
        ('宫格顺序', {'fields': ['grid_rank']}),
        ('是否删除', {'fields': ['is_deleted']}),
    ]
    list_per_page = 10


admin.site.register(Banner, BannerAdmin)
admin.site.register(Grid, GridAdmin)