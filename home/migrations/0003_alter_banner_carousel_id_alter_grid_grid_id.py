# Generated by Django 4.1.3 on 2022-11-17 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_grid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='carousel_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='grid',
            name='grid_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
