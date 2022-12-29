from django.db import models
from django.utils import timezone


# Create your models here.
class Banner(models.Model):
    carousel_id = models.AutoField(primary_key=True)
    carousel_url = models.CharField(max_length=100)
    redirect_url = models.CharField(max_length=100)
    carousel_rank = models.IntegerField()
    is_deleted = models.IntegerField(default=0)
    create_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'mall_carousel'

class Grid(models.Model):
    grid_id = models.AutoField(primary_key=True)
    grid_url = models.CharField(max_length=100)
    redirect_url = models.CharField(max_length=100)
    grid_sort = models.CharField(max_length=50)
    grid_rank = models.IntegerField()
    is_deleted = models.IntegerField(default=0)
    create_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'mall_grid'