# Generated by Django 3.2.6 on 2021-10-19 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0032_auto_20211019_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentvoucher',
            name='invoiceref',
        ),
        migrations.RemoveField(
            model_name='purchesinvoice',
            name='invoiceref',
        ),
        migrations.RemoveField(
            model_name='salseinvoice',
            name='invoiceref',
        ),
    ]
