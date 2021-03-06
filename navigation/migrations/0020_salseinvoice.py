# Generated by Django 3.2.6 on 2021-09-23 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0019_auto_20210923_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='salseinvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoiceno', models.CharField(blank=True, max_length=100000)),
                ('invoicedate', models.DateField()),
                ('invoiceref', models.CharField(max_length=30)),
                ('custmercode', models.CharField(blank=True, max_length=100000)),
                ('customeraddress', models.CharField(max_length=122)),
                ('customergstin', models.CharField(blank=True, max_length=30)),
                ('itemcode', models.CharField(blank=True, max_length=30)),
                ('desc', models.CharField(max_length=122)),
                ('uom', models.CharField(max_length=122)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('unitprice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('batchno', models.CharField(max_length=100000)),
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
