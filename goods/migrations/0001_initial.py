# Generated by Django 4.1.3 on 2022-11-18 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('goods_id', models.AutoField(primary_key=True, serialize=False)),
                ('goods_name', models.CharField(max_length=100, null=True)),
                ('goods_intro', models.CharField(max_length=100, null=True)),
                ('goods_category_id', models.IntegerField()),
                ('goods_cover_img', models.CharField(max_length=100, null=True)),
                ('goods_carousel', models.CharField(max_length=100, null=True)),
                ('goods_detail_content', models.CharField(max_length=100, null=True)),
                ('original_price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('stock_num', models.IntegerField(default=0, null=True)),
                ('tag', models.CharField(max_length=50)),
                ('goods_sell_status', models.IntegerField(default=0, null=True)),
                ('create_time', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'mall_goodsInfo',
            },
        ),
    ]
