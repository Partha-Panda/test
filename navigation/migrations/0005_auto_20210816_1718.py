# Generated by Django 3.2.6 on 2021-08-16 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0004_auto_20210816_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='itemcode',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vcode',
            field=models.CharField(blank=True, max_length=100000),
        ),
    ]
