# Generated by Django 3.2.6 on 2021-09-27 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0023_auto_20210927_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchesinvoice',
            name='amount',
            field=models.DecimalField(decimal_places=5, max_digits=8),
        ),
    ]
