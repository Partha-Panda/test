# Generated by Django 3.2.6 on 2021-09-20 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0017_pricingscheme'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricingscheme',
            name='profit',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=8),
        ),
    ]