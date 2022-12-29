from django.contrib import admin

# Register your models here.

from category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['Category_id', 'Category_name', 'category_rank', 'is_deleted', 'create_time']
    fieldsets = [
        ('分类ID', {'fields': ['Category_id']}),
        ('分类名称', {'fields': ['Category_name']}),
        ('分类排名', {'fields': ['category_rank']}),
        ('是否删除', {'fields': ['is_deleted']}),
    ]
    list_per_page = 10


admin.site.register(Category, CategoryAdmin)

