# Generated by Django 3.2.6 on 2021-09-17 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0015_auto_20210917_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchesinvoice',
            name='cgstamount',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='purchesinvoice',
            name='igstamount',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='purchesinvoice',
            name='sgstamount',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='purchesinvoice',
            name='totalamount',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]
