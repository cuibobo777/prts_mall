# Generated by Django 4.1.3 on 2022-12-21 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='goods_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]