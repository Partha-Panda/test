# Generated by Django 3.2.6 on 2021-09-27 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0020_salseinvoice'),
    ]

    operations = [
        migrations.CreateModel(
            name='paymentvoucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoiceno', models.CharField(max_length=100000)),
                ('invoiceref', models.CharField(max_length=30)),
                ('vcode', models.CharField(blank=True, max_length=100000)),
                ('vname', models.CharField(max_length=122)),
                ('vadd', models.CharField(max_length=122)),
                ('vengstin', models.CharField(blank=True, max_length=30)),
                ('itemcode', models.CharField(blank=True, max_length=30)),
                ('desc', models.CharField(max_length=122)),
                ('uom', models.CharField(max_length=122)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('unitprice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cgst', models.DecimalField(decimal_places=2, max_digits=5)),
                ('igst', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sgst', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cgstamount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('sgstamount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('igstamount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('totalamount', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
    ]
