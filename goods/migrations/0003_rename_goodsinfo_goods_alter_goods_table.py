# Generated by Django 4.1.3 on 2022-11-18 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_goodsinfo_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GoodsInfo',
            new_name='Goods',
        ),
        migrations.AlterModelTable(
            name='goods',
            table='mall_goods',
        ),
    ]
