# Generated by Django 3.2.6 on 2021-08-16 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0005_auto_20210816_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='itemcode',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
