# Generated by Django 3.2.6 on 2021-09-14 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0012_auto_20210914_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchesinvoice',
            name='vengstin',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
