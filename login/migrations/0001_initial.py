# Generated by Django 4.1.3 on 2022-12-12 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userAccount',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=32)),
                ('user_password', models.CharField(max_length=64)),
                ('user_token', models.CharField(blank=True, max_length=64, null=True)),
                ('is_deleted', models.IntegerField(default=0)),
                ('create_time', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'userInfo',
            },
        ),
    ]