# Generated by Django 4.1.3 on 2022-12-23 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0004_useraddress_area_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='userDetailInfo',
            fields=[
                ('user_detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('nick_name', models.CharField(max_length=32)),
                ('introduce', models.CharField(default='这个人很懒,什么也没有写', max_length=64)),
                ('PRTS_num', models.IntegerField(default=500, max_length=32)),
                ('pic_url', models.CharField(default='default_head_portrait_from_prts.png', max_length=100)),
                ('furniture_num', models.IntegerField(default=500, max_length=32)),
                ('is_deleted', models.IntegerField(default=0)),
                ('create_time', models.DateField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.useraccount')),
            ],
            options={
                'db_table': 'userdetail',
            },
        ),
    ]