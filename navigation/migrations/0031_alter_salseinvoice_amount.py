# Generated by Django 3.2.6 on 2021-10-18 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0030_auto_20211018_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salseinvoice',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]
